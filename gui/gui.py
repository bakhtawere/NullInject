import tkinter as tk
from tkinter import ttk, messagebox
import random
from modules import xss, sqli, cmdinj
from utils.encoder import encode
from utils.exporter import export_json
from utils.burp_integration import send_to_burp
from utils.zap_integration import send_to_zap

class NullInjectGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NullInject v1.0")
        self.root.geometry("800x600")
        self.setup_ui()

    def setup_ui(self):
        # Payload Type Selection
        ttk.Label(self.root, text="Payload Type:", font=("Arial", 12)).pack(pady=10)
        self.payload_type = ttk.Combobox(self.root, values=["XSS", "SQLi", "Command"])
        self.payload_type.pack()

        # Encoding Options
        ttk.Label(self.root, text="Encoding:", font=("Arial", 12)).pack(pady=10)
        self.encoding = ttk.Combobox(self.root, values=["None", "Base64", "URL", "Hex"])
        self.encoding.pack()

        # Generate Button
        ttk.Button(self.root, text="Generate Payload", command=self.generate).pack(pady=20)

        # Output Box
        self.output = tk.Text(self.root, height=10, width=80)
        self.output.pack()

        # Action Buttons
        ttk.Button(self.root, text="Copy to Clipboard", command=self.copy).pack(side=tk.LEFT, padx=10)
        ttk.Button(self.root, text="Export to JSON", command=self.export).pack(side=tk.LEFT)
        ttk.Button(self.root, text="Send to Burp", command=lambda: self.send("burp")).pack(side=tk.LEFT, padx=10)
        ttk.Button(self.root, text="Send to ZAP", command=lambda: self.send("zap")).pack(side=tk.LEFT)

    def generate(self):
        ptype = self.payload_type.get()
        payload = random.choice({
            "XSS": xss.get_xss_payloads(),
            "SQLi": sqli.get_sqli_payloads(),
            "Command": cmdinj.get_cmd_payloads()
        }[ptype])
        
        if self.encoding.get() != "None":
            payload = encode(payload, self.encoding.get().lower())
        
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, payload)

    def copy(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.output.get(1.0, tk.END))

    def export(self):
        export_json(self.output.get(1.0, tk.END))
        messagebox.showinfo("Success", "Payload exported to output/payloads.json")

    def send(self, tool):
        payload = self.output.get(1.0, tk.END)
        if tool == "burp":
            success = send_to_burp(payload)
        else:
            success = send_to_zap(payload)
        
        if success:
            messagebox.showinfo("Success", f"Sent to {tool.upper()}!")
        else:
            messagebox.showerror("Error", f"Failed to connect to {tool.upper()}")

def run_gui():
    root = tk.Tk()
    NullInjectGUI(root)
    root.mainloop()
