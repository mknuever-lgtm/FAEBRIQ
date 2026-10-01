from PIL import Image, ImageDraw, ImageFont, ImageChops
S='/tmp/claude-0/-home-user-FAEBRIQ/f8e84ab0-f651-5cf3-bfea-b2af690ad046/scratchpad/'
F='/root/.claude/skills/synced/c93a948f-a631-4152-b58b-61997870983b_07c67fa9-2b18-4383-88df-4830cdb0a99a/canvas-design/canvas-fonts/'
W,H=3000,1250; BG=(15,14,12); FG=(224,224,224); DIM=(70,68,64); FAINT=(26,25,22); ACC=(123,63,170)
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
mono=lambda s:ImageFont.truetype(F+'IBMPlexMono-Regular.ttf',s)
bod=lambda s,b=False:ImageFont.truetype(S+('bodoni-b.ttf' if b else 'bodoni.ttf'),s)
M=90
# measurement grid
for x in range(M,W-M+1,60): d.line([(x,M),(x,H-M)],fill=FAINT,width=1)
for y in range(M,H-M+1,60): d.line([(M,y),(W-M,y)],fill=FAINT,width=1)
# corner registration marks
for cx,cy in [(M,M),(W-M,M),(M,H-M),(W-M,H-M)]:
    d.line([(cx-22,cy),(cx+22,cy)],fill=DIM,width=2); d.line([(cx,cy-22),(cx,cy+22)],fill=DIM,width=2)
# edge annotations
f=mono(22)
d.text((M+40,M-56),'SYS/FAEBRIQ  ·  PROC 0x0F0E0C  ·  STATUS: UNEXPECTED',font=f,fill=DIM)
t='FAEBRIQ.COM'; d.text((W-M-40-d.textlength(t,font=f),M-56),t,font=f,fill=DIM)
d.text((M+40,H-M+30),'REF. 404 / 2026  ·  US + CA  ·  FREE SHIPPING',font=f,fill=DIM)
t='FIG. 01'; d.text((W-M-40-d.textlength(t,font=f),H-M+30),t,font=f,fill=DIM)
# dialog window, off-center right
dx0,dy0,dx1,dy1=1240,280,2700,940
d.rectangle([dx0+18,dy0+18,dx1+18,dy1+18],fill=(10,9,8))
d.rectangle([dx0,dy0,dx1,dy1],fill=BG,outline=FG,width=3)
d.line([(dx0,dy0+74),(dx1,dy0+74)],fill=FG,width=3)
d.text((dx0+36,dy0+22),'system_notice.exe',font=mono(26),fill=FG)
# window controls
for i in range(3):
    x=dx1-46-i*44; d.rectangle([x-12,dy0+25,x+12,dy0+49],outline=DIM,width=2)
# accent: single alert square
d.rectangle([dx0+60,dy0+150,dx0+108,dy0+198],fill=ACC)
# phrase lockup, Bodoni, line2 at 80%
L1=118; f1=bod(L1); f2=bod(int(L1*0.8))
tx=dx0+150
d.text((tx,dy0+122),'Unexpected',font=f1,fill=FG)
d.text((tx,dy0+122+L1*1.12),'identity detected.',font=f2,fill=FG)
d.text((tx,dy0+122+L1*1.12+L1*0.8*1.55),'This is not an error.',font=mono(28),fill=DIM)
# buttons
fb=mono(30); by=dy1-130
def btn(x,label,primary):
    w=int(d.textlength(label,font=fb))+80
    if primary: d.rectangle([x,by,x+w,by+72],fill=FG); d.text((x+40,by+18),label,font=fb,fill=BG)
    else: d.rectangle([x,by,x+w,by+72],outline=DIM,width=2); d.text((x+40,by+18),label,font=fb,fill=DIM)
    return w
r2='Wear it anyway'; w2=int(d.textlength(r2,font=fb))+80
x2=dx1-60-w2; btn(x2,r2,True)
r1='Ignore'; w1=int(d.textlength(r1,font=fb))+80; btn(x2-30-w1,r1,False)
# sans wordmark per assets/print-art/reference/wordmark-reference-2026-09-23.jpg,
# gapless six-block circuit bar at 1.35x wordmark width, centered beneath
fw=ImageFont.truetype(S+'inter0.ttf',150)
ww=d.textlength('FÆBRIQ',font=fw); bb=d.textbbox((0,0),'FÆBRIQ',font=fw)
bw=ww*1.35; wx=M+70; by0=H-M-110; bh=round(bw*0.016)
th=bb[3]-bb[1]; wy=by0-int(th*0.55)-th-bb[1]
d.text((wx+(bw-ww)/2,wy),'FÆBRIQ',font=fw,fill=FG)
CIRCUIT=[(232,39,42),(244,127,32),(249,212,38),(42,170,66),(29,91,190),(123,63,170)]
cw=bw/6
for i,c in enumerate(CIRCUIT): d.rectangle([round(wx+i*cw),by0,round(wx+(i+1)*cw)-1,by0+bh],fill=c)
d.text((wx,wy+bb[1]-70),'> process running',font=mono(24),fill=DIM)
im.save('hero-error-state-3000x1250.png'); print(bb, th)
