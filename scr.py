import sssh
s=sssh.Slide()
default='Times 10'
s.add_text('skuska',font=default)
s.add_text('toto je naozaj len a len skuska!!',font=default)
s.add_text('vlaky',font='Hack 10')
s.add_text('kazdy z nas uz niekedy cestoval vlakom.',font=default)
s.add_title(title='bla',color='orange',font='Castellar 50')
s.add_image(1000,110,'/home/adam/Downloads/dynboard.png')

a=sssh.Slide()
a.add_title('shshhshsh',font='OldEnglishTextMT 50',color='skyblue')
a.add_text('blah',font=default)
a.add_image(1000,110,'/home/adam/Downloads/dynboard.png' ) 
w=sssh.Slide()

q=sssh.Slide()
q.add_text('ahoj')
q.add_text('ahojahoj', font='KristenITC 20')
ad=sssh.SlideShow(q,w,a,s)
g=sssh.SlideShow(s,a,w,q)
g.play()
ad.play()

