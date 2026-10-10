# Builds the canonical 404 print files (big 404, one-line STRAIGHT NOT FOUND, stripe) from Maurice's 2026-09-23 reference. Run from the repo root.
import sys; sys.path.insert(0,'tools')
import make_print_file as m
from PIL import Image, ImageFont, ImageDraw
# Proportions measured off Maurice's 2026-09-23 reference, as fractions of bar width B.
R=dict(n404_w=0.2799, l2_w=0.7732, gap1=0.0642, gap2=0.0216, bar_h=0.0166, gap_mark=0.0510, mark_w=0.140)
def build(out,width,sticker,tote=False):
    # tote=True (Maurice, 2026-10-01): full phrase-width bar like apparel, plus
    # the approved sans FÆBRIQ wordmark underneath.
    sticker=sticker or tote
    serif=m.font_path("Bodoni Moda",None,"BodoniModa-Regular.ttf")
    col={k:tuple(int(v.lstrip('#')[i:i+2],16) for i in (0,2,4)) for k,v in m.INK_LIGHT.items()}
    pad=width*0.045; B=width-2*pad
    f1=m._fit(ImageFont,serif,"404",R['n404_w']*B,'w'); f2=m._fit(ImageFont,serif,"STRAIGHT NOT FOUND",R['l2_w']*B,'w')
    h1=f1.getbbox("404"); h1=h1[3]-h1[1]; h2=f2.getbbox("STRAIGHT NOT FOUND"); h2=h2[3]-h2[1]
    y1=pad; y2=y1+h1+R['gap1']*B; yb=y2+h2+R['gap2']*B; bh=R['bar_h']*B
    fm=None; bottom=yb+bh
    if sticker:
        fm=m._fit(ImageFont,serif,"FÆBRIQ",R['mark_w']*B,'w')
        hm=fm.getbbox("FÆBRIQ"); hm=hm[3]-hm[1]
        ym=yb+bh+R['gap_mark']*B; bottom=ym+hm
    im=Image.new('RGBA',(width,int(round(bottom+pad))),(0,0,0,0)); cx=width/2
    m._draw_reinforced(im,cx,y1,"404",f1,col['text']); m._draw_reinforced(im,cx,y2,"STRAIGHT NOT FOUND",f2,col['text'])
    d=ImageDraw.Draw(im)
    # Bar-to-wordmark ratio (Maurice, 2026-09-25): on the sticker, the bar is
    # 1.35x the FÆBRIQ mark's own width, not tied to the full canvas width B.
    # The apparel file (sticker=False) has no mark, so it keeps the old
    # full-width bar -- nothing for it to be 1.35x of.
    bar_w = m.BAR_TO_MARK_RATIO * fm.getlength("FÆBRIQ") if sticker and not tote else B
    sw, gap = m.SRC['stripe_frac']*bar_w, m.SRC['gap_frac']*bar_w
    bx = cx - bar_w/2
    for i,c in enumerate(m.CIRCUIT): x0=bx+i*(sw+gap); d.rectangle([x0,yb,x0+sw,yb+bh],fill=c)
    if tote:
        mb=fm.getbbox("FÆBRIQ"); mark=m.wordmark_mask(fm.getlength("FÆBRIQ"),col['mark']+(255,))
        im.alpha_composite(mark,(round(cx-mark.width/2),round(ym+mb[1]+((mb[3]-mb[1])-mark.height)/2)))
    elif sticker: m._draw_reinforced(im,cx,ym,"FÆBRIQ",fm,col['mark'])
    im.save(out,'PNG',dpi=(300,300)); print(out,im.size)
# Pass targets (apparel, sticker, tote) to build only those; no args builds all.
want=set(sys.argv[1:]) or {'apparel','sticker','tote'}
if 'apparel' in want: build('assets/print-art/404-straight-not-found-v3-light-4500.png',4500,False)
if 'sticker' in want: build('assets/print-art/sticker-final-system-2026-08-27/404-straight-not-found-v3-sticker-light-2400.png',2400,True)
if 'tote' in want: build('assets/print-art/404-straight-not-found-v3-tote-light-4500.png',4500,False,tote=True)
