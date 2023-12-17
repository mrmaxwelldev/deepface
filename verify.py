from deepface.DeepFace import verify

result = verify("e1.jpg", "e2.jpg")

if result["verified"]:
  print("True")
else:
  print("False")
