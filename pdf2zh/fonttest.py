# from pathlib import Path

# font_path = Path(r"C:\Users\Srijan\Desktop\Mytest\pdf translate\PDFMathTranslate\pdf2zh\NotoSansDevanagari-Regular.ttf")

# if font_path.exists():
#     print("✅ Font found:", font_path)
# else:
#     print("❌ Font not found:", font_path)

hindi_text = "नमस्ते दुनिया"
encoded_text = hindi_text.encode("utf-8")
print(encoded_text.decode("utf-8"))
