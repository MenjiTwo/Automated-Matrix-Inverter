import tkinter as tk
from tkinter import messagebox, ttk
import sympy as sp
import re
import ctypes

def to_subscript(n):
    return "".join("₀₁₂₃₄₅₆₇₈₉"[int(d)] for d in str(n))

class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command=None, width=120, height=40, radius=15, 
                 bg_color="#e0e0e0", fg_color="black", hover_bg="#d0d0d0", font=("Segoe UI", 11)):
        super().__init__(parent, width=width, height=height, bg=parent["bg"], highlightthickness=0)
        self.command = command
        self.radius = radius
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.hover_bg = hover_bg
        self.font = font
        self.normal_bg = bg_color
        self.rect_id = self.create_rounded_rect(2, 2, width-2, height-2, radius, fill=bg_color, outline="")
        self.text_id = self.create_text(width/2, height/2, text=text, fill=fg_color, font=font)
        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def create_rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
        points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
        return self.create_polygon(points, **kwargs, smooth=True)

    def on_click(self, event):
        if self.command: self.command()

    def on_enter(self, event):
        self.itemconfig(self.rect_id, fill=self.hover_bg)

    def on_leave(self, event):
        self.itemconfig(self.rect_id, fill=self.normal_bg)

    def update_colors(self, bg, fg, hover):
        self.normal_bg = bg
        self.fg_color = fg
        self.hover_bg = hover
        self.itemconfig(self.rect_id, fill=bg)
        self.itemconfig(self.text_id, fill=fg)
        self.configure(bg=self.master["bg"])
        
    def config_text(self, text):
        self.itemconfig(self.text_id, text=text)

class RoundedEntry(tk.Canvas):
    def __init__(self, parent, width_px=80, height_px=35, radius=10, font=("Segoe UI", 12), justify='center'):
        super().__init__(parent, width=width_px, height=height_px, bg=parent["bg"], highlightthickness=0)
        self.radius = radius
        self.rect_id = self.create_rounded_rect(2, 2, width_px-2, height_px-2, radius, fill="white", outline="#cccccc")
        self.entry = tk.Entry(self, font=font, justify=justify, bd=0, highlightthickness=0, bg="white", fg="gray")
        self.entry.place(relx=0.5, rely=0.5, anchor='center', width=width_px-15, height=height_px-10)
        self.entry.insert(0, "0")
        self.entry.bind("<FocusIn>", self.on_focus_in)
        self.entry.bind("<FocusOut>", self.on_focus_out)
        self.external_focus_in = None
        self.external_focus_out = None

    def create_rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
        points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
        return self.create_polygon(points, **kwargs, smooth=True)

    def on_focus_in(self, event):
        if self.external_focus_in: self.external_focus_in(event) 

    def on_focus_out(self, event):
        if self.external_focus_out: self.external_focus_out(event)

    def get(self):
        return self.entry.get()

    def update_colors(self, entry_bg, entry_fg, border_color, parent_bg):
        self.configure(bg=parent_bg)
        self.itemconfig(self.rect_id, fill=entry_bg, outline=border_color)
        self.entry.configure(bg=entry_bg, fg=entry_fg)

class MatrixInverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automated Matrix Inverter")
        self.first_launch = True
        self.matrix_size = 2
        self.entry_widgets = []
        self.dark_mode = False 
        self.theme_btn = None 
        self.last_w = 0
        self.last_h = 0
        self.tree_border = None 
        self.result_border = None
        self.legend_border = None
        self.show_decimals = False
        self.stored_original = None
        self.stored_inverse = None
        self.content_wrapper = None
        self.convert_btn = None

        self.root.minsize(700, 500)
        self.colors = {
            "light": {
                "bg_main": "#f0f0f0", "bg_container": "#f0f0f0", "fg_text": "black",
                "fg_subtle": "gray", "entry_bg": "#ffffff", "entry_fg": "gray", "entry_fg_active": "black", 
                "btn_bg": "#e0e0e0", "btn_fg": "black", "btn_hover": "#d0d0d0",
                "btn_accent": "#d0f0c0", "btn_accent_hover": "#c0e0b0",
                "tree_bg": "#f0f0f0", "tree_fg": "black", "tree_select": "#0078D7",
                "accent_orig": "#8B0000", "accent_inv": "#006400", "border": "#cccccc"
            },
            "dark": {
                "bg_main": "#2b2b2b", "bg_container": "#2b2b2b", "fg_text": "#ffffff",
                "fg_subtle": "#aaaaaa", "entry_bg": "#383838", "entry_fg": "#aaaaaa", "entry_fg_active": "#ffffff", 
                "btn_bg": "#404040", "btn_fg": "#ffffff", "btn_hover": "#505050",
                "btn_accent": "#2ecc71", "btn_accent_hover": "#27ae60",
                "tree_bg": "#2b2b2b", "tree_fg": "#ffffff", "tree_select": "#0078D7",
                "accent_orig": "#ff6b6b", "accent_inv": "#5cdb95", "border": "#555555"
            }
        }
        self.style = ttk.Style()
        self.create_theme_toggle()
        self.show_size_selection()

    def get_current_colors(self):
        return self.colors["dark"] if self.dark_mode else self.colors["light"]

    def create_theme_toggle(self):
        self.theme_btn = tk.Button(self.root, text="⏾", font=("Segoe UI", 16), command=self.toggle_dark_mode, bd=0, relief="flat", cursor="hand2")
        self.theme_btn.place(relx=1.0, rely=1.0, anchor="se", x=-20, y=-20, width=40, height=40)
        self.theme_btn.bind("<Enter>", lambda e: self.theme_btn.configure(bg="#999" if self.dark_mode else "#bbb"))
        self.theme_btn.bind("<Leave>", lambda e: self.apply_theme_to_widget(self.theme_btn, force_btn=True))
        self.apply_theme() 

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def update_title_bar(self):
        try:
            hwnd = ctypes.windll.user32.GetParent(self.root.winfo_id())
            is_dark = 1 if self.dark_mode else 0
            ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, 20, ctypes.byref(ctypes.c_int(is_dark)), 4)
            c = self.get_current_colors()
            bg_hex = c["bg_main"].lstrip('#')
            r, g, b = tuple(int(bg_hex[i:i+2], 16) for i in (0, 2, 4))
            color_ref = (b << 16) | (g << 8) | r
            ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, 35, ctypes.byref(ctypes.c_int(color_ref)), 4)
            text_color_ref = 0x00FFFFFF if self.dark_mode else 0x00000000
            ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, 36, ctypes.byref(ctypes.c_int(text_color_ref)), 4)
        except Exception: pass

    def apply_theme(self):
        c = self.get_current_colors()
        self.root.configure(bg=c["bg_main"], bd=0, highlightthickness=0)
        self.root.update() 
        self.update_title_bar()
        self.style.theme_use('clam') 
        self.style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        self.style.configure("Treeview", background=c["tree_bg"], foreground=c["tree_fg"], fieldbackground=c["tree_bg"], font=("Segoe UI", 11), rowheight=35, borderwidth=0, relief="flat") 
        self.style.configure("Treeview.Heading", background=c["btn_bg"], foreground=c["btn_fg"], font=("Segoe UI", 10, "bold"), relief="flat", borderwidth=0)
        self.style.map("Treeview", background=[('selected', c["tree_select"])])
        self.style.configure("TCombobox", fieldbackground=c["btn_bg"], background=c["btn_bg"], foreground=c["btn_fg"], arrowcolor=c["btn_fg"], borderwidth=0, relief="flat", darkcolor=c["btn_bg"], lightcolor=c["btn_bg"])
        self.style.map("TCombobox", fieldbackground=[('readonly', c["btn_bg"]), ('disabled', c["bg_main"])], background=[('readonly', c["btn_bg"]), ('disabled', c["bg_main"])], foreground=[('readonly', c["btn_fg"]), ('disabled', c["fg_subtle"])], arrowcolor=[('readonly', c["btn_fg"]), ('disabled', c["fg_subtle"])], selectbackground=[('readonly', c["btn_bg"]), ('!readonly', c["btn_bg"])], selectforeground=[('readonly', c["btn_fg"]), ('!readonly', c["btn_fg"])])
        self.recurse_apply_theme(self.root)
        if self.theme_btn:
            self.theme_btn.lift()
            self.theme_btn.configure(bg=c["bg_container"], fg=c["fg_text"])

    def recurse_apply_theme(self, widget):
        c = self.get_current_colors()
        if widget == self.theme_btn: return
        w_type = widget.winfo_class()
        try:
            if isinstance(widget, RoundedButton):
                is_accent = (widget.bg_color in ["#d0f0c0", "#2ecc71"])
                new_bg = c["btn_accent"] if is_accent else c["btn_bg"]
                new_fg = "black" if is_accent else c["btn_fg"]
                new_hover = c["btn_accent_hover"] if is_accent else c["btn_hover"]
                widget.bg_color = new_bg 
                widget.update_colors(new_bg, new_fg, new_hover)
            elif isinstance(widget, RoundedEntry):
                val = widget.get()
                current_entry_fg = widget.entry.cget("fg")
                is_empty_zero = (val == "0" and str(current_entry_fg) in ["gray", "#aaaaaa"])
                fg_col = c["entry_fg"] if is_empty_zero else c["entry_fg_active"]
                parent_bg = c["bg_container"] if "Frame" in str(widget.master) else (c["bg_main"] if widget.master == self.root else c["bg_container"])
                widget.update_colors(c["entry_bg"], fg_col, c["border"], parent_bg)
            elif w_type == 'Frame':
                widget.configure(bd=0, highlightthickness=0)
                if getattr(widget, 'is_tree_border', False): widget.configure(bg=c["btn_bg"]) 
                elif widget.master == self.root: widget.configure(bg=c["bg_main"])
                else: widget.configure(bg=c["bg_container"])
            elif w_type == 'Label':
                current_fg = widget.cget("fg")
                if current_fg in ["#8B0000", "#ff6b6b"]: widget.configure(fg=c["accent_orig"])
                elif current_fg in ["#006400", "#5cdb95"]: widget.configure(fg=c["accent_inv"])
                elif current_fg in ["gray", "#aaaaaa"]: widget.configure(fg=c["fg_subtle"])
                else: widget.configure(fg=c["fg_text"])
                widget.configure(bg=c["bg_container"])
            elif w_type == 'Canvas' and not isinstance(widget, (RoundedButton, RoundedEntry)):
                widget.configure(bg=c["bg_container"], highlightthickness=0, bd=0)
                for item in widget.find_withtag("bracket"):
                    curr_fill = widget.itemcget(item, "fill")
                    if curr_fill in ["#8B0000", "#ff6b6b"]: widget.itemconfig(item, fill=c["accent_orig"])
                    elif curr_fill in ["#006400", "#5cdb95"]: widget.itemconfig(item, fill=c["accent_inv"])
        except Exception: pass 
        for child in widget.winfo_children():
            self.recurse_apply_theme(child)

    def apply_theme_to_widget(self, widget, force_btn=False):
        c = self.get_current_colors()
        if force_btn: widget.configure(bg=c["bg_container"], fg=c["fg_text"])

    def set_window_geometry(self, width, height):
        self.root.update_idletasks()
        try:
            if self.root.state() == 'zoomed': return 
        except tk.TclError: pass
        if not self.first_launch:
            curr_w, curr_h = self.root.winfo_width(), self.root.winfo_height()
            if abs(curr_w - self.last_w) > 50 or abs(curr_h - self.last_h) > 50: return
        screen_width, screen_height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        width = min(width, screen_width - 50)
        height = min(height, screen_height - 50)
        if self.first_launch:
            x, y = (screen_width // 2) - (width // 2), (screen_height // 2) - (height // 2)
            self.root.geometry(f'{int(width)}x{int(height)}+{int(x)}+{int(y)}')
            self.first_launch = False
        else:
            match = re.match(r"(\d+)x(\d+)\+([-\d]+)\+([-\d]+)", self.root.geometry())
            if match:
                curr_w, curr_h, curr_x, curr_y = map(int, match.groups())
                new_x, new_y = curr_x + (curr_w - width) // 2, curr_y + (curr_h - height) // 2
                self.root.geometry(f'{int(width)}x{int(height)}+{int(new_x)}+{int(new_y)}')
            else:
                self.root.geometry(f'{int(width)}x{int(height)}')
        self.last_w, self.last_h = width, height

    def clear_window(self):
        for widget in self.root.winfo_children():
            if widget != self.theme_btn: widget.destroy()

    def show_size_selection(self):
        self.clear_window()
        self.set_window_geometry(750, 550)
        container = tk.Frame(self.root)
        container.place(relx=0.5, rely=0.5, anchor='center')
        tk.Label(container, text="Select Matrix Size", font=("Segoe UI", 18, "bold")).pack(pady=(0, 0))
        tk.Label(container, text="Supports 2-10", font=("Segoe UI", 10, "italic"), fg="gray").pack(pady=(0, 0))
        sizes = [str(i) for i in range(2, 11)]
        self.size_var = tk.StringVar(value="2")
        self.size_combo = ttk.Combobox(container, textvariable=self.size_var, values=sizes, state="readonly", width=5, font=("Segoe UI", 12), justify='center')
        self.size_combo.pack(pady=(15, 0))
        RoundedButton(container, text="Generate Matrix", command=self.validate_size, width=140, height=40, radius=15).pack(pady=(15, 0))
        self.apply_theme() 

    def validate_size(self):
        try:
            self.matrix_size = int(self.size_var.get())
            self.show_input_grid()
        except ValueError:
            messagebox.showerror("Error", "Invalid selection.")

    def show_input_grid(self):
        self.clear_window()
        self.show_decimals = False 
        base_w, base_h = 750, 550
        extra_w = max(0, (self.matrix_size - 4) * 60) 
        extra_h = max(0, (self.matrix_size - 4) * 40)
        self.set_window_geometry(base_w + extra_w, base_h + extra_h)
        main_wrapper = tk.Frame(self.root)
        main_wrapper.place(relx=0.5, rely=0.5, anchor='center')
        tk.Label(main_wrapper, text=f"Input {self.matrix_size}x{self.matrix_size} Matrix", font=("Segoe UI", 18, "bold")).pack(pady=(0, 0))
        tk.Label(main_wrapper, text="Click a cell to edit : Supports variables (a, b, c, etc...)", font=("Segoe UI", 10, "italic"), fg="gray").pack(pady=(0, 2))
        grid_frame = tk.Frame(main_wrapper)
        grid_frame.pack(pady=(2, 0))
        self.entry_widgets = []
        for r in range(self.matrix_size):
            row_entries = []
            for c in range(self.matrix_size):
                e = RoundedEntry(grid_frame, width_px=80, height_px=40, radius=10, font=("Segoe UI", 12))
                e.grid(row=r, column=c, padx=3, pady=3)
                e.external_focus_in = self.on_entry_focus_in
                e.external_focus_out = self.on_entry_focus_out
                row_entries.append(e)
            self.entry_widgets.append(row_entries)
        ctrl_frame = tk.Frame(main_wrapper)
        ctrl_frame.pack(pady=(10, 0))
        RoundedButton(ctrl_frame, text="Back", command=self.show_size_selection, width=140, height=40).pack(side=tk.LEFT, padx=10)
        RoundedButton(ctrl_frame, text="Calculate", command=self.process_inverse, width=140, height=40, bg_color="#d0f0c0").pack(side=tk.LEFT, padx=10)
        self.apply_theme() 

    def on_entry_focus_in(self, event):
        c = self.get_current_colors()
        event.widget.configure(fg=c["entry_fg_active"])
        if event.widget.get() == "0": event.widget.delete(0, tk.END)

    def on_entry_focus_out(self, event):
        c = self.get_current_colors()
        if not event.widget.get().strip():
            event.widget.insert(0, "0")
            event.widget.configure(fg=c["entry_fg"])
        else:
            event.widget.configure(fg=c["entry_fg_active"])

    def process_inverse(self):
        try:
            matrix_data = []
            for r in range(self.matrix_size):
                row_data = []
                for c in range(self.matrix_size):
                    val_str = self.entry_widgets[r][c].get().strip()
                    if not val_str: val_str = "0"
                    
                    try:
                        val = sp.Rational(val_str)
                    except (ValueError, TypeError):
                        val = val_str
                        
                    row_data.append(val)
                matrix_data.append(row_data)
                
            sym_matrix = sp.Matrix(matrix_data)
            inverse_matrix, steps_data = self.gauss_jordan_elimination(sym_matrix)
            self.show_results(sym_matrix, inverse_matrix, steps_data)
        except ValueError as e:
            msg = "This matrix has a determinant of zero.\nIt does not have an inverse." if str(e) == "Singular Matrix" else f"{e}"
            messagebox.showinfo("Singular Matrix", msg)
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred.\n{e}")

    def gauss_jordan_elimination(self, matrix):
        n = matrix.rows
        M = matrix.hstack(matrix, sp.eye(n)).as_mutable()
        steps = []
        for i in range(n):
            pivot = M[i, i]
            if pivot == 0:
                for k in range(i + 1, n):
                    if M[k, i] != 0:
                        M.row_swap(i, k)
                        steps.append(('swap', i+1, k+1, None))
                        pivot = M[i, i]
                        break
                else:
                    raise ValueError("Singular Matrix")
            if pivot != 1:
                M.row_op(i, lambda x, j: x / pivot)
                M = sp.simplify(M).as_mutable()
                steps.append(('scale', i+1, None, 1/pivot))
            for k in range(n):
                if k != i:
                    factor = M[k, i]
                    if factor != 0:
                        M.row_op(k, lambda x, j: x - factor * M[i, j])
                        M = sp.simplify(M).as_mutable()
                        steps.append(('add', k+1, i+1, -factor))
        return M[:, n:], steps

    def show_results(self, original, inverse, raw_steps):
        self.stored_original = original
        self.stored_inverse = inverse
        
        self.clear_window()
        c = self.get_current_colors()
        req_width = 850 + (self.matrix_size * 20)
        req_height = 600 + (self.matrix_size * 10)
        self.set_window_geometry(req_width, req_height)
        
        footer_frame = tk.Frame(self.root, height=60)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        btn_frame = tk.Frame(footer_frame)
        btn_frame.pack(pady=15)
        
        btn_text = "To Decimal" if not self.show_decimals else "To Fraction"
        self.convert_btn = RoundedButton(btn_frame, text=btn_text, command=self.toggle_format, width=140, height=40, radius=15)
        self.convert_btn.pack(side=tk.LEFT, padx=10)

        RoundedButton(btn_frame, text="New Matrix", command=self.show_size_selection, width=140, height=40, radius=15).pack(side=tk.LEFT, padx=10)
        
        main_container = tk.Frame(self.root)
        main_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=20, pady=10)
        main_container.columnconfigure(0, weight=3)
        main_container.columnconfigure(1, weight=1)
        main_container.rowconfigure(0, weight=1)
        
        left_outer_frame = tk.Frame(main_container, bd=0, highlightthickness=0)
        left_outer_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 15))
        self.result_border = tk.Frame(left_outer_frame, height=2, bd=0, highlightthickness=0)
        self.result_border.pack(side=tk.BOTTOM, fill=tk.X)
        self.result_border.is_tree_border = True 
        left_canvas = tk.Canvas(left_outer_frame, highlightthickness=0)
        visuals_frame = tk.Frame(left_canvas)
        visuals_frame.bind("<Configure>", lambda e: left_canvas.configure(scrollregion=left_canvas.bbox("all")))
        canvas_window = left_canvas.create_window((0, 0), window=visuals_frame, anchor="nw")
        left_canvas.bind("<Configure>", lambda e: left_canvas.itemconfig(canvas_window, width=e.width))
        left_canvas.pack(side=tk.LEFT, fill="both", expand=True)
        left_outer_frame.bind("<Enter>", lambda e: left_canvas.bind_all("<MouseWheel>", lambda ev: left_canvas.yview_scroll(int(-1*(ev.delta/120)), "units")))
        
        self.content_wrapper = tk.Frame(visuals_frame)
        self.content_wrapper.pack(expand=True, fill='x', pady=20)
        
        self.refresh_matrix_view()

        right_frame = tk.Frame(main_container)
        right_frame.grid(row=0, column=1, sticky="nsew")
        tk.Label(right_frame, text="Elementary Row Operations", font=("Segoe UI", 12, "bold")).pack(side=tk.TOP, pady=(0, 10))
        legend_frame = tk.Frame(right_frame)
        legend_frame.pack(side=tk.BOTTOM, fill='x', pady=(10, 0))
        tk.Label(legend_frame, text="Gauss-Jordan Operations", font=("Segoe UI", 12, "bold")).pack(pady=(0, 5))
        legend_box = tk.Frame(legend_frame, bd=0, highlightthickness=0)
        legend_box.pack(fill='both')
        legend_text = "Type I - Swap row i and row j.\nType II - Multiply row i by a nonzero scalar.\nType III - Replace row i by the sum of row i\n               and nonzero scalar times row j."
        tk.Label(legend_box, text=legend_text, justify="left", anchor="w", font=("Segoe UI", 11), padx=10, pady=10).pack(fill='both')
        self.legend_border = tk.Frame(legend_frame, height=2, bd=0, highlightthickness=0)
        self.legend_border.pack(side=tk.BOTTOM, fill=tk.X)
        self.legend_border.is_tree_border = True 
        tree_container = tk.Frame(right_frame, bd=0, highlightthickness=0)
        tree_container.pack(side=tk.TOP, fill='both', expand=True)
        self.tree_border = tk.Frame(tree_container, height=2, bd=0, highlightthickness=0)
        self.tree_border.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree_border.is_tree_border = True 
        tree = ttk.Treeview(tree_container, columns=("Type", "Operations"), show='headings')
        tree.heading("Type", text="Type")
        tree.heading("Operations", text="Operations")
        tree.column("Type", width=50, anchor="center")
        tree.column("Operations", width=220)
        tree.pack(side=tk.LEFT, fill='both', expand=True)
        tree_container.bind("<Enter>", lambda e: tree.bind_all("<MouseWheel>", lambda ev: tree.yview_scroll(int(-1*(ev.delta/120)), "units")))
        for op_type, r1, r2, val in raw_steps:
            if op_type == 'swap':
                tree.insert("", tk.END, values=("I", f"E{to_subscript(r1)+to_subscript(r2)}"))
            elif op_type == 'scale':
                tree.insert("", tk.END, values=("II", f"E{to_subscript(r1)}({str(val).replace('**', '^').replace('*', '')})"))
            elif op_type == 'add':
                tree.insert("", tk.END, values=("III", f"E{to_subscript(r1)+to_subscript(r2)}({str(val).replace('**', '^').replace('*', '')})"))
        self.apply_theme() 

    def refresh_matrix_view(self):
        if not self.content_wrapper: return
        
        for widget in self.content_wrapper.winfo_children():
            widget.destroy()
            
        tk.Label(self.content_wrapper, text="Original Matrix", font=("Segoe UI", 12, "bold"), fg="#8B0000").pack(pady=(0, 10))
        self.render_matrix_native(self.content_wrapper, self.stored_original, "orig")
        tk.Label(self.content_wrapper, text="Inverse Result", fg="#006400", font=("Segoe UI", 12, "bold")).pack(pady=(40, 10))
        self.render_matrix_native(self.content_wrapper, self.stored_inverse, "inv")
        
        self.recurse_apply_theme(self.content_wrapper)

    def toggle_format(self):
        self.show_decimals = not self.show_decimals
        new_text = "To Fraction" if self.show_decimals else "To Decimal"
        self.convert_btn.config_text(new_text)
        self.refresh_matrix_view()

    def format_cell(self, val):
        if self.show_decimals:
            try:
                if val.is_number: 
                    f_val = float(val)
                    if f_val.is_integer():
                        return str(int(f_val))
                    return f"{f_val:.4f}".rstrip('0')
            except Exception:
                pass 

        if isinstance(val, sp.Rational) and val.q != 1:
            p, q = val.p, val.q
            if p < 0: p = -p
            s_num, s_den = ("-" if val.p < 0 else "") + str(p), str(q)
            width = max(len(s_num), len(s_den))
            return f"{s_num.center(width)}\n{'-' * width}\n{s_den.center(width)}"
        return sp.pretty(val, use_unicode=False)

    def render_matrix_native(self, parent, matrix, tag):
        c = self.get_current_colors()
        container = tk.Frame(parent)
        container.pack(pady=10)
        accent_color = c["accent_orig"] if tag=="orig" else c["accent_inv"]
        grid_frame = tk.Frame(container)
        for r_idx, row in enumerate(matrix.tolist()):
            for c_idx, val in enumerate(row):
                tk.Label(grid_frame, text=self.format_cell(val), font=("Consolas", 10), fg=accent_color).grid(row=r_idx, column=c_idx, padx=10, pady=5)
        grid_frame.update_idletasks()
        h = grid_frame.winfo_reqheight()
        left_canvas = tk.Canvas(container, width=15, height=h, highlightthickness=0)
        right_canvas = tk.Canvas(container, width=15, height=h, highlightthickness=0)
        bracket_col = c["accent_orig"] if tag=="orig" else c["accent_inv"]
        left_canvas.create_line(12, 2, 2, 2, 2, h-2, 12, h-2, fill=bracket_col, width=2, capstyle="round", tags="bracket")
        right_canvas.create_line(2, 2, 12, 2, 12, h-2, 2, h-2, fill=bracket_col, width=2, capstyle="round", tags="bracket")
        left_canvas.pack(side=tk.LEFT)
        grid_frame.pack(side=tk.LEFT, padx=5)
        right_canvas.pack(side=tk.LEFT)

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixInverterApp(root)
    root.mainloop()