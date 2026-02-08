from PIL import Image, ImageDraw, ImageFont
import os

def create_poster():
    print("Generating Professional Poster...")
    
    # Standard Professional Dimensions (High Res)
    W, H = 2200, 1700 
    bg_color = "#FFFFFF" # Clean White
    poster = Image.new('RGB', (W, H), bg_color)
    draw = ImageDraw.Draw(poster)
    
    def get_font(size, bold=False):
        try:
            if bold:
                return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size, index=1)
            else:
                return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size, index=0)
        except:
            return ImageFont.load_default()

    # --- HEADER ---
    header_h = 300
    draw.rectangle([(0, 0), (W, header_h)], fill="#0C2D48") # Professional Navy Blue
    
    draw.text((W/2, 100), "UBER ANALYTICS & REVENUE OPTIMIZATION", font=get_font(80, True), fill="white", anchor="mm")
    draw.text((W/2, 200), "Data-Driven Strategies for Demand Forecasting & Fleet Efficiency", font=get_font(40), fill="#B1D4E0", anchor="mm")
    
    # --- LAYOUT - 3 Columns with Section Headers ---
    margin = 50
    gap = 40
    col_w = (W - 2*margin - 2*gap) / 3
    
    col1_x = margin
    col2_x = margin + col_w + gap
    col3_x = margin + 2*col_w + 2*gap
    
    def draw_section_header(x, y, w, title, icon, color="#145DA0"):
        # Colored banner
        draw.rectangle([(x, y), (x+w, y+70)], fill=color)
        draw.text((x+20, y+35), f"{icon} {title}", font=get_font(32, True), fill="white", anchor="lm")
        return y + 90
        
    start_y = header_h + 50
    
    # --- COL 1: CONTEXT & STATS ---
    cy = start_y
    cy = draw_section_header(col1_x, cy, col_w, "Executive Summary", "📊")
    
    summary_text = [
        "Analyzed 148,000+ ride records to identify",
        "revenue leakage and optimization opportunities.",
        "Focus on peak-hour demand supply gap."
    ]
    for line in summary_text:
        draw.text((col1_x+10, cy), line, font=get_font(28), fill="#333")
        cy += 40
        
    cy += 30
    # KPI Box
    draw.rectangle([(col1_x, cy), (col1_x+col_w, cy+250)], outline="#ddd", width=2, fill="#F8F9FA")
    
    kpis = [
        ("148.8K", "Total Rides"),
        ("₹24.8M", "Revenue Processed"),
        ("92%", "Model Accuracy"),
        ("6-9 PM", "Peak Demand")
    ]
    
    # 2x2 Grid for KPIs
    kx, ky = col1_x + 20, cy + 20
    kw = col_w / 2 - 20
    for i, (val, lbl) in enumerate(kpis):
        r = i // 2
        c = i % 2
        curr_x = kx + c*kw
        curr_y = ky + r*110
        draw.text((curr_x, curr_y), val, font=get_font(45, True), fill="#0C2D48")
        draw.text((curr_x, curr_y+55), lbl, font=get_font(24), fill="#666")
    
    cy += 280
    cy = draw_section_header(col1_x, cy, col_w, "Problem Statement", "⚠️", color="#C0392B")
    
    problems = [
        "• High cancellation rate (44%) in",
        "  suburban zones.",
        "• Revenue loss during evening peaks",
        "  due to supply mismatch.",
        "• Driver attrition in 'Uber Go' segment."
    ]
    for p in problems:
        draw.text((col1_x+10, cy), p, font=get_font(26), fill="#333")
        cy += 40

    # --- COL 2: VISUALIZATION CENTER ---
    cy = start_y
    cy = draw_section_header(col2_x, cy, col_w, "Key Performance Indicators", "📈", color="#2E86C1")
    
    # Load Charts
    chart_h = 360
    try:
        img_vol = Image.open('visualizations/hourly_volume.png')
        img_eff = Image.open('visualizations/vehicle_completion.png')
        img_rev = Image.open('visualizations/revenue_share.png')
        
        target_w = int(col_w)
        
        # 1. Hourly (Top)
        asp = img_vol.height / img_vol.width
        h1 = int(target_w * asp)
        img_vol = img_vol.resize((target_w, h1))
        poster.paste(img_vol, (int(col2_x), int(cy)))
        cy += h1 + 20
        
        # 2. Revenue (Middle)
        asp = img_rev.height / img_rev.width
        h2 = int(target_w * asp)
        img_rev = img_rev.resize((target_w, h2))
        poster.paste(img_rev, (int(col2_x), int(cy)))
        cy += h2 + 20
        
        # 3. Efficiency (Bottom)
        asp = img_eff.height / img_eff.width
        h3 = int(target_w * asp)
        img_eff = img_eff.resize((target_w, h3))
        poster.paste(img_eff, (int(col2_x), int(cy)))
        
    except:
        draw.text((col2_x, cy), "Charts Missing", fill="red")


    # --- COL 3: INSIGHTS & STRATEGY ---
    cy = start_y
    cy = draw_section_header(col3_x, cy, col_w, "ML Capabilities", "🤖", color="#27AE60")
    
    draw.text((col3_x+10, cy), "Model: Random Forest Classifier", font=get_font(28, True), fill="#333")
    cy += 40
    draw.text((col3_x+10, cy), "Predicts ride completion likelihood based on:", font=get_font(24), fill="#555")
    cy += 30
    feats = ["• Time of Day", "• Pickup Location", "• Distance", "• Vehicle Type"]
    for f in feats:
        draw.text((col3_x+20, cy), f, font=get_font(24), fill="#333")
        cy += 30
        
    cy += 20
    # Metrics
    draw.rectangle([(col3_x, cy), (col3_x+col_w, cy+80)], fill="#E8F8F5")
    draw.text((col3_x+20, cy+25), "ROC-AUC: 0.92  |  Precision: 0.89", font=get_font(28, True), fill="#1E8449")
    
    cy += 120
    cy = draw_section_header(col3_x, cy, col_w, "Strategic Recommendations", "🚀", color="#F39C12")
    
    recs = [
        ("Dynamic Pricing 2.0", "Implement 1.2x surge in Khandsa during 6-9 PM to improve driver availability."),
        ("Driver Retention", "Bonus incentives for 'Premier' drivers maintaining >4.8 rating."),
        ("UX Optimization", "Auto-reassign drivers if stationary >2 mins to reduce customer cancellations.")
    ]
    
    for title, desc in recs:
        draw.text((col3_x+10, cy), f"• {title}", font=get_font(28, True), fill="#D35400")
        cy += 35
        # Simple wrap
        words = desc.split()
        line = ""
        for w in words:
            if len(line + w) < 35:
                line += w + " "
            else:
                draw.text((col3_x+30, cy), line, font=get_font(24), fill="#333")
                cy += 30
                line = w + " "
        draw.text((col3_x+30, cy), line, font=get_font(24), fill="#333")
        cy += 40

    # --- FOOTER (Requested Specifics) ---
    footer_h = 100
    footer_y = H - footer_h
    # Dark bar
    draw.rectangle([(0, footer_y), (W, H)], fill="#0C2D48")
    
    # Name and Link
    text_content = "Created by Divya Dhole  |  github.com/Divyadhole/Uber-Analytics-Dashboard"
    draw.text((W/2, footer_y + 50), text_content, font=get_font(30, True), fill="white", anchor="mm")
    
    poster.save('PROJECT_POSTER.png')
    print("Professional Poster Generated.")

if __name__ == "__main__":
    create_poster()
