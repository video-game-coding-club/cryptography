code_text = """ofoxlopyboroqydovomdbymedon,tkcyxgkcrkfsxqkbyddoxnki.rogyuosxdrolkmucokdypkcmryyvlec,xydcebogroborogkc,ryvnsxqrkxncgsdrkqsbvronsnx'duxyg.drkdgkcx'dxomocckbsvidrobyddoxzkbd.droqsbvgkcmedo,ledromyevnx'dpsqeboyedgrycrogkcybgrkdrogkcnysxqdrobo.rockdezkxnbellonrscoioc,dbisxqdydrsxu.kpognyjoxusncczbkgvonsxdrocokdcsxpbyxdyprsw,vscdoxsxqdyszync,dkvusxq,ybcvoozsxq.droikvvvyyuonkbyexnrsckqo...pspdoox?cshdoox?yuki,drkdgkccmkbi.ronsnx'duxygrscygxkqo.drolecbewlvonkvyxqklewzibykn.yeddrogsxnygc,nocobdbyvvonliexnobklbsqrdlveocui.tkcyxgkczboddiceboronsnx'dvsfosxdronocobd .rodbsondydrsxulkmu...drovkcddrsxqrobowowlobon...droqsbvcaeoojonrscrkxn."tkcyx,iyeyuki?"crogybopknontokxc,rsusxqlyydc,kxnkpvoomocxyglykbnsxqtkmuod.robmrymyvkdolbygxrksbgkcmedmryzzikxnexofox,gsdrdrsxcdbkxnclbksnonnygxdrocsnoc.crogyboxywkuoez,vsuocrogkcdbisxqxyddynbkgkddoxdsyxdyrobcovp;ledsdnsnx'dgybu.crogkccobsyecvizboddi.roboioccoowondymrkxqomyvybv suokukvosnycmyzo-lbygx,lveo,kxnqboox.tkcyxvodqyyprobrkxn."ew,snyx'd-"sxdropbyxdypdrolec,kdokmrobcryedon,"kvvbsqrd,mezmkuoc,vscdoxez!"droqeigkcylfsyecvikmykmr.rsclkcolkvvmkzgkczevvonvygyfobrscrksb,cyiyemyevntecdcoorscloknioioc.rorknkgscziqykdookxnkcyebpkmo,vsuoro'nokdoxcywodrsxqwyvni.rscleppkbwckxnmrocdzecronkqksxcdklbsqrdybkxqozyvycrsbd.rscxivyxgybuyedzkxdckxnxsuocgoboczydvoccgrsdo.kgrscdvorexqpbywrscxomu,kxnkwoqkzryxogkcmvszzondyrsclovd.rogyevn'fovyyuonzboddicmkbisprorknx'dlooxpsfopyydjoby.groxrocdyynezsxdrokscvo,yxoypdrocdenoxdcmkvvon,"cdkxnez,mykmrronqo!""srokbndrkd!"dromykmrcmkxxondrolecpybdroyppoxnob.droxrscoiocpshonyxtkcyx,kxnrsccmygvnoozoxon.ktyvdgoxdnygxtkcyx'cczsxo.rogkccebodromykmruxogronsnx'dlovyxqdrobo.rogkcqysxqdymkvvtkcyxyed,nowkxngrkdrogkcnysxqyxdrolec?kxntkcyxgyevnx'drkfokmveogrkddycki.ledmykmrronqovyyuonkgkikxnmvokbonrscdrbykd."go'vvkbbsfosxpsfowsxedoc!cdkigsdriyebzkbdxob.nyx'dvycoiyebgybucrood.kxnspkxiypiyezbomsyecvsddvomezmkuocmkecokxidbyelvoyxdrscdbsz,sgsvvzobcyxkvvicoxniyelkmudymkwzecdrorkbngki."rozsmuonezklkcolkvvlkdkxnwknovsuorogkcrsdd"""
p_shift = 10  # char position shift for cypher

# 'p' for "position"
p0 = 97  # starting point for ascii chars
for i in range(26):
  p_real = p0 + i
  p_code = p_real + p_shift
  if(p_code > p0+25): p_code = p_code-26
  s_code = chr(p_code)
  s_real = chr(p_real)
  code_text = code_text.replace(s_code,s_real.upper())
  #print(s_code,s_real.upper())

print(code_text)


