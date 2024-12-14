import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

class TextToSpeechApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Text to Speech")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")
        
        self.create_widgets()

    def create_widgets(self):
        """إنشاء الواجهة الرسومية"""
        # العنوان الرئيسي
        header = tk.Label(self.root, text="Text to Speech", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
        header.pack(pady=10)

        # التعليمات
        sub_header = tk.Label(self.root, text="Enter your text below:", font=("Arial", 12), bg="#f0f0f0", fg="#555")
        sub_header.pack()

        # إدخال النص
        self.text_entry = tk.Entry(self.root, width=40, font=("Arial", 14), justify="center", bd=2, relief="solid")
        self.text_entry.pack(pady=10)

        # أزرار التحكم
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=20)

        play_button = tk.Button(button_frame, text="Play", font=("Arial", 12, "bold"), bg="#4caf50", fg="white", width=10, command=self.play_text)
        play_button.grid(row=0, column=0, padx=10)

        reset_button = tk.Button(button_frame, text="Reset", font=("Arial", 12, "bold"), bg="#2196f3", fg="white", width=10, command=self.reset_text)
        reset_button.grid(row=0, column=1, padx=10)

        exit_button = tk.Button(button_frame, text="Exit", font=("Arial", 12, "bold"), bg="#f44336", fg="white", width=10, command=self.exit_program)
        exit_button.grid(row=0, column=2, padx=10)

        # الفوتر
        footer = tk.Label(self.root, text="Created by Abdullah", font=("Arial", 10), bg="#f0f0f0", fg="#999")
        footer.pack(side="bottom", pady=10)

    def play_text(self):
        """تشغيل النص المدخل كنطق صوتي"""
        text = self.text_entry.get()
        if text.strip():
            tts = gTTS(text=text, lang='en')
            tts.save("output.mp3")
            os.system("start output.mp3" if os.name == "nt" else "afplay output.mp3")
        else:
            messagebox.showwarning("تحذير", "يرجى إدخال النص أولاً!")

    def reset_text(self):
        """إعادة تعيين النص المدخل"""
        self.text_entry.delete(0, tk.END)

    def exit_program(self):
        """إغلاق التطبيق"""
        self.root.destroy()

# تشغيل التطبيق
if _name_ == "_main_":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()