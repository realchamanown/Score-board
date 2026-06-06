import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("light") 
ctk.set_default_color_theme("blue")  

class ScoreEntryApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ระบบคีย์คะแนนทีม 💻")
        self.geometry("500x600")
        self.resizable(False, False)

        self.team_data = {}

        # --------- topic ----------
        ctk.CTkLabel(self, text="📋 ระบบคีย์คะแนนทีม", font=("SF Pro Display", 20, "bold")).pack(pady=20)

        # ---------- form ----------
        entry_frame = ctk.CTkFrame(self, fg_color="white")
        entry_frame.pack(pady=10, padx=20, fill="both", expand=False)

        # teamname
        ctk.CTkLabel(entry_frame, text="ชื่อทีม:", font=("SF Pro Display", 14)).pack(anchor="w", padx=20, pady=(15, 0))
        self.team_entry = ctk.CTkEntry(entry_frame, font=("SF Pro Display", 14))
        self.team_entry.pack(padx=20, pady=5, fill="x")

        # score
        ctk.CTkLabel(entry_frame, text="คะแนน (จำนวนเต็มบวก):", font=("SF Pro Display", 14)).pack(anchor="w", padx=20, pady=(10, 0))
        self.score_entry = ctk.CTkEntry(entry_frame, font=("SF Pro Display", 14))
        self.score_entry.pack(padx=20, pady=5, fill="x")

        # time
        ctk.CTkLabel(entry_frame, text="เวลา (หน่วย: นาที):", font=("SF Pro Display", 14)).pack(anchor="w", padx=20, pady=(10, 0))
        self.time_entry = ctk.CTkEntry(entry_frame, font=("SF Pro Display", 14))
        self.time_entry.pack(padx=20, pady=15, fill="x")

        # ---------- button ----------
        ctk.CTkButton(self, text="💾 บันทึกข้อมูลทีม", command=self.save_data, font=("SF Pro Display", 14), width=300).pack(pady=10)
        ctk.CTkButton(self, text="📊 สรุปผลและจัดอันดับ", command=self.show_ranking, font=("SF Pro Display", 14), width=300).pack(pady=5)

        # ---------- result ----------
        ctk.CTkLabel(self, text="ผลการจัดอันดับ", font=("SF Pro Display", 15, "bold"), text_color="blue").pack(pady=10)
        self.rank_text = ctk.CTkTextbox(self, height=250, font=("SF Pro Display", 13))
        self.rank_text.pack(padx=20, fill="both", expand=True)

    def save_data(self):
        team = self.team_entry.get().strip()
        try:
            score = int(self.score_entry.get())
            time = float(self.time_entry.get())
            if score < 0 or time < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("ข้อผิดพลาด", "กรุณาใส่คะแนนและเวลาให้ถูกต้อง (คะแนนจำนวนเต็ม, เวลาเป็นนาที)")
            return

        if not team:
            messagebox.showwarning("เตือน", "กรุณากรอกชื่อทีม")
            return

        self.team_data[team] = (score, time)
        self.team_entry.delete(0, "end")
        self.score_entry.delete(0, "end")
        self.time_entry.delete(0, "end")
        messagebox.showinfo("สำเร็จ", f"บันทึกข้อมูลให้ทีม '{team}' แล้ว")

    def show_ranking(self):
        if not self.team_data:
            messagebox.showinfo("ไม่มีข้อมูล", "ยังไม่มีการกรอกข้อมูลทีมใด")
            return

        ranked = sorted(self.team_data.items(), key=lambda x: (-x[1][0], x[1][1]))
        self.rank_text.delete("1.0", "end")
        for i, (team, (score, time)) in enumerate(ranked, start=1):
            self.rank_text.insert("end", f"{i}. {team} - {score} คะแนน, {time:.2f} นาที\n")

# ---------- app ----------
if __name__ == "__main__":
    app = ScoreEntryApp()
    app.mainloop()
