# Cet exemple de code montre comment numériser des images et extraire du texte
import aspose.ocr as ocr

# Initialiser le moteur OCR
api = ocr.AsposeOcr()

# Ajouter une image au lot de reconnaissance
input = ocr.OcrInput(ocr.InputType.SINGLE_IMAGE)
input.add("pb_ss_fond.png")

# Reconnaître l'image
result = api.recognize(input)

# Résultat de la reconnaissance d'impression
print(result[0].recognition_text)