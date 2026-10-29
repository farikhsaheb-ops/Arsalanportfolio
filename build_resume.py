#!/usr/bin/env python3
"""Regenerate resume.pdf from RESUME_DATA. Edit verified details in this structure first."""
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, Flowable
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import HexColor
from pathlib import Path

RESUME_DATA = {
    "name": "ARSALAN WARISH",
    "title": "Python Developer | Web Designer | Graphic Designer",
    "email": "dartioarsalan07@gmail.com",
    "phone": "+91 73209 69935",
    "location": "Rohini, Delhi, India",
    "portfolio_url": "https://example.com/",  # Replace after deployment.
    "summary": "Independent digital creative focused on Python programming, responsive web design and professional graphic design. Values clear communication, practical solutions and thoughtful visual detail.",
    "key_points": [("5+ Years Experience", "Verify professional timeline before publishing."), ("1000+ Projects", "Confirm and adjust the figure if needed."), ("New & Modern Technology", "AI · Automation · Cloud · Modern Web")],
    "skills": [("Python programming", 82), ("Automation & scraping", 76), ("Data processing", 72), ("HTML & CSS", 86), ("JavaScript", 74), ("Responsive UI", 78), ("Visual design", 84), ("Brand identity", 79), ("Design systems", 80)],
    "tools": ["Python", "Flask", "FastAPI", "Django", "Pandas", "NumPy", "Selenium", "Git", "HTML5", "CSS3", "JavaScript", "Figma", "Photoshop", "Illustrator", "Canva"],
    "services": [("Python Programming", "Automation scripts, custom tools, web scraping, data processing, APIs and workflow utilities."), ("Web Designing", "Responsive websites, landing pages, portfolio sites, UI styling and brand-led web experiences."), ("Professional Graphic Design", "Brand identity, logo systems, social campaign assets, stationery and packaging concepts.")],
    "experience": [
        {"role": "Independent digital creative", "period": "DATES / DETAILS TO BE CONFIRMED", "detail": "Replace with verified work history, project scope and measurable outcomes."},
        {"role": "Selected project", "period": "PROJECT / YEAR TO BE ADDED", "detail": "Add a real project, the problem addressed, your contribution and the result."},
    ],
    "education": "Add verified qualification, institution and year. No degree or school has been assumed.",
    "certifications": "Add verified certification title, issuing organization and date — or remove if not applicable.",
    "languages": "English · Hindi (edit proficiency)",
}
OUT = Path(__file__).with_name("resume.pdf")
INK=HexColor('#20243a'); MUTED=HexColor('#626b80'); VIOLET=HexColor('#7564d9'); LINE=HexColor('#dce0ec'); PALE=HexColor('#f3f4fb')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Name',fontName='Helvetica-Bold',fontSize=23,leading=25,textColor=colors.white,spaceAfter=2))
styles.add(ParagraphStyle(name='Role',fontName='Helvetica',fontSize=9,leading=12,textColor=HexColor('#e7e5ff')))
styles.add(ParagraphStyle(name='Contact',fontName='Helvetica',fontSize=6.6,leading=9,textColor=colors.white))
styles.add(ParagraphStyle(name='SectionV3',fontName='Helvetica-Bold',fontSize=8.5,leading=10,textColor=VIOLET,spaceBefore=5,spaceAfter=5))
styles.add(ParagraphStyle(name='BodyV3',fontName='Helvetica',fontSize=7.3,leading=10,textColor=INK,spaceAfter=3))
styles.add(ParagraphStyle(name='MutedV3',fontName='Helvetica',fontSize=6.6,leading=8.4,textColor=MUTED,spaceAfter=3))
styles.add(ParagraphStyle(name='ItemTitleV3',fontName='Helvetica-Bold',fontSize=7.6,leading=9,textColor=INK,spaceAfter=1))
styles.add(ParagraphStyle(name='MetaV3',fontName='Courier',fontSize=5.7,leading=7,textColor=VIOLET,spaceAfter=2))
styles.add(ParagraphStyle(name='SkillV3',fontName='Helvetica',fontSize=6.5,leading=8,textColor=INK))
styles.add(ParagraphStyle(name='ChipV3',fontName='Helvetica',fontSize=6,leading=8,textColor=INK))
styles.add(ParagraphStyle(name='FootV3',fontName='Courier',fontSize=5.5,leading=7,textColor=MUTED))
def P(s,style='BodyV3'): return Paragraph(s,styles[style])
def section(title, content): return [P(title.upper(),'SectionV3')]+content

class QRFlowable(Flowable):
    def __init__(self, value, size=34*mm): super().__init__(); self.value=value; self.width=size; self.height=size
    def draw(self):
        widget=qr.QrCodeWidget(self.value); bounds=widget.getBounds(); w=bounds[2]-bounds[0]; h=bounds[3]-bounds[1]
        drawing=Drawing(self.width,self.height, transform=[self.width/w,0,0,self.height/h,0,0]); drawing.add(widget); renderPDF.draw(drawing,self.canv,0,0)

def on_page(canvas,doc):
    canvas.saveState(); w,h=A4
    # layered gradient-like header band, crisp vector shapes and accent geometry
    canvas.setFillColor(HexColor('#24203f')); canvas.rect(0,h-49*mm,w,49*mm,fill=1,stroke=0)
    canvas.setFillColor(HexColor('#6555bc')); canvas.rect(w*.52,h-49*mm,w*.48,49*mm,fill=1,stroke=0)
    canvas.setFillColor(HexColor('#76c8d1')); canvas.circle(w-7*mm,h-4*mm,28*mm,fill=1,stroke=0)
    canvas.setFillColor(HexColor('#6555bc')); canvas.circle(w-10*mm,h-4*mm,24*mm,fill=1,stroke=0)
    canvas.setStrokeColor(HexColor('#ffffff88')); canvas.setLineWidth(.8); canvas.roundRect(13*mm,h-26*mm,14*mm,14*mm,4*mm,fill=0,stroke=1)
    canvas.setFillColor(colors.white); canvas.setFont('Helvetica-Bold',9); canvas.drawCentredString(20*mm,h-18*mm,'A/W')
    canvas.setFont('Helvetica-Bold',21); canvas.drawString(32*mm,h-18*mm,RESUME_DATA['name'])
    canvas.setFillColor(HexColor('#e7e5ff')); canvas.setFont('Helvetica',8); canvas.drawString(32*mm,h-24*mm,RESUME_DATA['title'])
    canvas.setFillColor(colors.white); canvas.setFont('Helvetica',6.3)
    contacts=f"✉  {RESUME_DATA['email']}     |     ☎  {RESUME_DATA['phone']}     |     ⌖  {RESUME_DATA['location']}"
    canvas.drawString(13*mm,h-34*mm,contacts)
    canvas.drawString(13*mm,h-40*mm,'↗  Portfolio: '+RESUME_DATA['portfolio_url'])
    canvas.setFillColor(PALE); canvas.rect(0,0,w,8*mm,fill=1,stroke=0)
    canvas.setFillColor(MUTED); canvas.setFont('Courier',5.5); canvas.drawString(13*mm,3*mm,'ARSALAN WARISH  ·  PYTHON  ·  WEB  ·  DESIGN')
    canvas.drawRightString(w-13*mm,3*mm,'RESUME / 2026  ·  EDIT VERIFIED DETAILS BEFORE SENDING')
    canvas.restoreState()

def sync_key_points_from_site_config():
    """Use the canonical key-point list from the top-level JS config for the PDF."""
    import re
    js_path=Path(__file__).with_name('js')/'script.js'
    source=js_path.read_text(encoding='utf-8')
    match=re.search(r"KEY_POINTS:\[(.*?)\],\n  SKILL_LEVELS",source,re.S)
    if not match: raise ValueError('Could not find SITE_CONFIG.KEY_POINTS in js/script.js')
    pairs=re.findall(r"\{value:'([^']+)',label:'([^']+)'\}",match.group(1))
    if len(pairs)!=3: raise ValueError('Expected exactly three key points in SITE_CONFIG.KEY_POINTS')
    RESUME_DATA['key_points']=[(value+' '+label.title(), 'Shared from SITE_CONFIG.KEY_POINTS in js/script.js.') for value,label in pairs]

def build():
    sync_key_points_from_site_config()
    w,h=A4; left=58*mm; right=118*mm; gap=7*mm; top=h-52*mm; bottom=11*mm
    doc=BaseDocTemplate(str(OUT),pagesize=A4,leftMargin=13*mm,rightMargin=13*mm,topMargin=51*mm,bottomMargin=10*mm,title='Arsalan Warish Resume',author='Arsalan Warish')
    frame_left=Frame(13*mm,bottom,left,top-bottom,id='left',leftPadding=0,rightPadding=5*mm,topPadding=0,bottomPadding=0)
    frame_right=Frame(13*mm+left+gap,bottom,w-26*mm-left-gap,top-bottom,id='right',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id='resume',frames=[frame_left,frame_right],onPage=on_page)])
    # Use two frames and frame-break to create a compact, selectable-text two-column document.
    from reportlab.platypus import FrameBreak
    story=[]
    story+=section('Profile',[P(RESUME_DATA['summary'])])
    story+=section('Key points',[P('<b>'+a+'</b><br/><font color="#626b80">'+b+'</font>','BodyV3') for a,b in RESUME_DATA['key_points']])
    story+=section('Core skills',[])
    for name,val in RESUME_DATA['skills']:
        t=Table([[P(name,'SkillV3'),P(f'<b>{val}%</b>','SkillV3')],[Table([['']],colWidths=[left*val/100],rowHeights=[3],style=TableStyle([('BACKGROUND',(0,0),(-1,-1),VIOLET),('BOX',(0,0),(-1,-1),0,colors.white)]))]],colWidths=[left-12*mm,12*mm])
        t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'MIDDLE'),('ALIGN',(1,0),(1,0),'RIGHT'),('SPAN',(0,1),(-1,1)),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),1),('BOTTOMPADDING',(0,0),(-1,-1),1)]));story.extend([t,Spacer(1,2)])
    story+=section('Tools & technology',[P(' · '.join(RESUME_DATA['tools']),'MutedV3')])
    story+=section('Languages',[P(RESUME_DATA['languages'],'MutedV3')])
    story.append(FrameBreak())
    story+=section('Services offered',[KeepTogether([P('<b>'+name+'</b>','ItemTitleV3'),P(desc,'MutedV3'),Spacer(1,3)]) for name,desc in RESUME_DATA['services']])
    story+=section('Experience & selected work',[])
    for e in RESUME_DATA['experience']:
        story.append(KeepTogether([P(e['role'],'ItemTitleV3'),P(e['period'],'MetaV3'),P(e['detail'],'MutedV3'),Spacer(1,5)]))
    story+=section('Education',[P(RESUME_DATA['education'],'MutedV3')])
    story+=section('Certifications',[P(RESUME_DATA['certifications'],'MutedV3')])
    story+=section('Portfolio QR code',[QRFlowable(RESUME_DATA['portfolio_url'],size=24*mm),Spacer(1,3),P('This QR encodes the portfolio_url value above. Replace the placeholder URL and regenerate the PDF after deployment.','MutedV3')])
    doc.build(story)
    print(f'Created {OUT}')
if __name__=='__main__': build()
