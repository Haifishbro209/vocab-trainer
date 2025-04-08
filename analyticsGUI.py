import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

class AnalyticsUI:
    def __init__(self, root, back_callback, vocab_data=None):
        self.root = root
        self.back_callback = back_callback
        self.vocab_data = vocab_data or []  # Beispieldaten falls keine übergeben wurden
        
        # Hauptframe für die Analytics-Ansicht
        self.main_frame = tk.Frame(root, bg='#1a1a1a')
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Statistik-Anzeige oben
        self.stats_frame = tk.Frame(self.main_frame, bg='#1a1a1a')
        self.stats_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Statistik-Widgets
        self.create_stats_widgets()
        
        # Graph-Anzeige in der Mitte
        self.graph_frame = tk.Frame(self.main_frame, bg='#1a1a1a')
        self.graph_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Graph erstellen
        self.create_graph()
        
        # Button-Frame unten
        self.button_frame = tk.Frame(self.main_frame, bg='#1a1a1a')
        self.button_frame.pack(fill=tk.X, padx=20, pady=20)
        
        # Zurück-Button
        back_button = tk.Button(
            self.button_frame, 
            text="Zurück", 
            bg='#2a2a2a', 
            fg='#00ff00', 
            font=('Arial', 14), 
            padx=15, 
            pady=3, 
            command=self.on_back
        )
        back_button.pack(side=tk.LEFT)
        
        # Filter-Widgets auf der rechten Seite
        filter_button = tk.Button(
            self.button_frame, 
            text="Filter", 
            bg='#2a2a2a', 
            fg='#00ff00', 
            font=('Arial', 14), 
            padx=15, 
            pady=3, 
            command=self.show_filter_options
        )
        filter_button.pack(side=tk.RIGHT)
        
        # Export-Button
        export_button = tk.Button(
            self.button_frame, 
            text="Exportieren", 
            bg='#2a2a2a', 
            fg='#00ff00', 
            font=('Arial', 14), 
            padx=15, 
            pady=3, 
            command=self.export_data
        )
        export_button.pack(side=tk.RIGHT, padx=10)
    
    def create_stats_widgets(self):
        # Statistik-Widgets erstellen
        stats_boxes = [
            {"label": "Gesamtanzahl\nVokabeln", "value": str(len(self.vocab_data))},
            {"label": "Durchschnittliche\nFehlerrate", "value": f"{self.calculate_avg_error_rate():.1f}%"},
            {"label": "Höchste\nFehlerrate", "value": f"{self.calculate_max_error_rate():.1f}%"},
            {"label": "Verbesserte\nVokabeln", "value": str(self.calculate_improved_words())},
        ]
        
        for i, stat in enumerate(stats_boxes):
            stat_frame = tk.Frame(self.stats_frame, bg='#2a2a2a', padx=15, pady=10)
            stat_frame.grid(row=0, column=i, padx=10, pady=5)
            
            label = tk.Label(
                stat_frame, 
                text=stat["label"], 
                bg='#2a2a2a', 
                fg='#00ff00', 
                font=('Arial', 12)
            )
            label.pack()
            
            value = tk.Label(
                stat_frame, 
                text=stat["value"], 
                bg='#2a2a2a', 
                fg='#00ff00', 
                font=('Arial', 18, 'bold')
            )
            value.pack(pady=5)
    
    def create_graph(self):
        # Figure und Axes erstellen
        self.fig, self.ax = plt.subplots(figsize=(10, 5))
        self.fig.patch.set_facecolor('#1a1a1a')
        self.ax.set_facecolor('#2a2a2a')
        
        # Beispieldaten für den Graphen
        if not self.vocab_data:
            # Wenn keine Daten vorhanden, Beispieldaten verwenden
            dates = [datetime.now().replace(day=d) for d in range(1, 15)]
            error_rates = [80, 75, 70, 72, 65, 68, 60, 55, 50, 48, 45, 40, 38, 35]
            vocab_counts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
        else:
            # Echte Daten verwenden
            dates = [datetime.strptime(item[2], "%Y-%m-%d %H:%M:%S") for item in self.vocab_data]
            error_rates = [float(item[1]) for item in self.vocab_data]
            vocab_counts = list(range(1, len(self.vocab_data) + 1))
        
        # Plot für Fehlerrate
        color = '#00ff00'
        self.ax.plot(dates, error_rates, marker='o', color=color, linewidth=2, label='Fehlerrate')
        self.ax.set_ylabel('Fehlerrate (%)', color=color, fontsize=12)
        self.ax.tick_params(axis='y', labelcolor=color)
        self.ax.grid(True, linestyle='--', alpha=0.7, color='#3a3a3a')
        
        # Zweite Y-Achse für Vokabelanzahl
        ax2 = self.ax.twinx()
        color = '#ff9900'
        ax2.plot(dates, vocab_counts, marker='s', color=color, linewidth=2, label='Vokabelanzahl')
        ax2.set_ylabel('Gesamtanzahl Vokabeln', color=color, fontsize=12)
        ax2.tick_params(axis='y', labelcolor=color)
        
        # X-Achse formatieren
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.'))
        self.ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
        plt.xticks(rotation=45)
        
        # Titel und Legende
        self.ax.set_title('Vokabeln & Fehlerrate über Zeit', color='#ffffff', fontsize=14)
        
        # Legende
        lines1, labels1 = self.ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        self.ax.legend(lines1 + lines2, labels1 + labels2, loc='upper center', 
                      bbox_to_anchor=(0.5, -0.15), ncol=2, facecolor='#2a2a2a', edgecolor='#3a3a3a')
        
        # Textfarben setzen
        for label in (self.ax.get_xticklabels() + self.ax.get_yticklabels() + ax2.get_yticklabels()):
            label.set_color('#ffffff')
        
        # Layout anpassen
        plt.tight_layout()
        
        # Canvas erstellen und in Frame einbetten
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def show_filter_options(self):
        # Filter-Dialog
        filter_dialog = tk.Toplevel(self.root)
        filter_dialog.geometry("300x250")
        filter_dialog.title("Filter")
        filter_dialog.configure(bg='#1a1a1a')
        
        tk.Label(filter_dialog, text="Zeitraum:", bg='#1a1a1a', fg='#00ff00', font=('Arial', 12)).pack(pady=(20, 5))
        
        options = ["Letzte Woche", "Letzter Monat", "Letztes Jahr", "Alle"]
        time_var = tk.StringVar(value=options[0])
        time_dropdown = ttk.Combobox(filter_dialog, textvariable=time_var, values=options, state="readonly")
        time_dropdown.pack(pady=5)
        
        tk.Label(filter_dialog, text="Vokabeln anzeigen:", bg='#1a1a1a', fg='#00ff00', font=('Arial', 12)).pack(pady=(15, 5))
        
        show_var = tk.StringVar(value="Alle")
        r1 = tk.Radiobutton(filter_dialog, text="Alle", variable=show_var, value="Alle", bg='#1a1a1a', fg='#00ff00', selectcolor='#2a2a2a')
        r1.pack(anchor=tk.W, padx=100)
        r2 = tk.Radiobutton(filter_dialog, text="Nur problematische", variable=show_var, value="Problematische", bg='#1a1a1a', fg='#00ff00', selectcolor='#2a2a2a')
        r2.pack(anchor=tk.W, padx=100)
        
        # Buttons
        button_frame = tk.Frame(filter_dialog, bg='#1a1a1a')
        button_frame.pack(fill=tk.X, pady=20)
        
        apply_button = tk.Button(button_frame, text="Anwenden", bg='#2a2a2a', fg='#00ff00', font=('Arial', 12), padx=10, pady=3, command=lambda: self.apply_filter(time_var.get(), show_var.get(), filter_dialog))
        apply_button.pack(side=tk.RIGHT, padx=10)
        
        cancel_button = tk.Button(button_frame, text="Abbrechen", bg='#2a2a2a', fg='#00ff00', font=('Arial', 12), padx=10, pady=3, command=filter_dialog.destroy)
        cancel_button.pack(side=tk.RIGHT, padx=10)
    
    def apply_filter(self, time_period, show_type, dialog):
        # Filter anwenden (hier nur als Platzhalter)
        print(f"Filter angewendet: {time_period}, {show_type}")
        dialog.destroy()
        
        # Hier würde man die Daten filtern und den Graph neu zeichnen
        # Für diese Demo aktualisieren wir einfach den Graphen
        self.update_graph(time_period, show_type)
    
    def update_graph(self, time_period, show_type):
        # Graph aktualisieren
        self.ax.clear()
        
        # Beispieldaten für den Graphen basierend auf Filtern
        if time_period == "Letzte Woche":
            dates = [datetime.now().replace(day=d) for d in range(8, 15)]
            error_rates = [60, 55, 50, 48, 45, 40, 38]
            vocab_counts = [40, 45, 50, 55, 60, 65, 70]
        else:
            dates = [datetime.now().replace(day=d) for d in range(1, 15)]
            error_rates = [80, 75, 70, 72, 65, 68, 60, 55, 50, 48, 45, 40, 38, 35]
            vocab_counts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
        
        # Plot für Fehlerrate
        self.ax.plot(dates, error_rates, marker='o', color='#00ff00', linewidth=2, label='Fehlerrate')
        self.ax.set_ylabel('Fehlerrate (%)', color='#00ff00', fontsize=12)
        self.ax.tick_params(axis='y', labelcolor='#00ff00')
        self.ax.grid(True, linestyle='--', alpha=0.7, color='#3a3a3a')
        
        # Zweite Y-Achse für Vokabelanzahl
        ax2 = self.ax.twinx()
        ax2.plot(dates, vocab_counts, marker='s', color='#ff9900', linewidth=2, label='Vokabelanzahl')
        ax2.set_ylabel('Gesamtanzahl Vokabeln', color='#ff9900', fontsize=12)
        ax2.tick_params(axis='y', labelcolor='#ff9900')
        
        # X-Achse formatieren
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.'))
        self.ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
        plt.xticks(rotation=45)
        
        # Titel und Legende
        self.ax.set_title(f'Vokabeln & Fehlerrate ({time_period}, {show_type})', color='#ffffff', fontsize=14)
        
        # Legende
        lines1, labels1 = self.ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        self.ax.legend(lines1 + lines2, labels1 + labels2, loc='upper center', 
                      bbox_to_anchor=(0.5, -0.15), ncol=2, facecolor='#2a2a2a', edgecolor='#3a3a3a')
        
        # Textfarben setzen
        for label in (self.ax.get_xticklabels() + self.ax.get_yticklabels() + ax2.get_yticklabels()):
            label.set_color('#ffffff')
        
        # Layout anpassen
        plt.tight_layout()
        self.canvas.draw()
    
    def export_data(self):
        # Export-Dialog
        export_dialog = tk.Toplevel(self.root)
        export_dialog.geometry("300x150")
        export_dialog.title("Exportieren")
        export_dialog.configure(bg='#1a1a1a')
        
        tk.Label(export_dialog, text="Format wählen:", bg='#1a1a1a', fg='#00ff00', font=('Arial', 12))

