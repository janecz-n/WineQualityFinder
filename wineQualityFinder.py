#!/usr/bin/python3

infile = "./winequality-red.csv"
# "fixed acidity";"volatile acidity";"citric acid";"residual sugar";"chlorides";"free sulfur dioxide";"total sulfur dioxide";"density";"pH";"sulphates";"alcohol";"quality"

PHMED = 3.31
PHMIN = 2.72


def main():
    firstline = 1
    result = []
    with open(infile) as inf:
        i = 0
        line_words = (line.split(';') for line in inf)
        for values in line_words:
            if firstline:
                firstline = 0
                continue
            # delete \n
            values[-1:] = values[-1:][0]
            values.pop()
            # grab values
            pH = values[-4]
            alcohol = values[-2]
            sulphates = values[-3]
            quality = values[-1]
            acidcitric = values[2]
            totalSulphure = values[-6]
            # totaldiff 0.5528327704815513, maxdiff 3.0165
            calculatedQuality = (float(alcohol) * 0.45) - ((float(pH) - PHMED) * 0.4) + (float(sulphates) * 1.35) + (float(acidcitric) * 0.1) - (float(totalSulphure) * 0.0035)
            result += [(pH, alcohol, sulphates, quality, format(calculatedQuality, '.2f'), format((float(quality) - calculatedQuality), '.4f'))]
            print ("Wine n°" + str(i))
            print ("  pH: " + pH + "\n  alcohol: " +  alcohol + "\n  suplhates: " + sulphates + "\n  quality: " + quality)
            print ("Our calculated quality: %.2f (diff: %f)" % (calculatedQuality, float(quality) - calculatedQuality))
            print ("------------")
            i += 1
        totalDiff = 0.0
        minDiff = 10
        maxDiff = 0
        for r in result:
            diff = float(r[-1])
            powDiff = abs(diff)
            if powDiff < minDiff:
                minDiff = powDiff
            if powDiff > maxDiff:
                maxDiff = powDiff
            totalDiff += powDiff
        print ("maxDiff")
        print (maxDiff)
        print ("totalDiff")
        print (totalDiff / i)


if __name__ == "__main__":
    main()
