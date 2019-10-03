code_text = \
    """ofoxlopyboroqydovomdbymedon,tkcyxgkcrkfsxqkbyddoxnki.rogyuosxdrolkmuco
kdypkcmryyvlec,xydcebogroborogkc,ryvnsxqrkxncgsdrkqsbvronsnx'duxyg.drk
dgkcx'dxomocckbsvidrobyddoxzkbd.droqsbvgkcmedo,ledromyevnx'dpsqeboyedg
rycrogkcybgrkdrogkcnysxqdrobo.rockdezkxnbellonrscoioc,dbisxqdydrsxu.kp
ognyjoxusncczbkgvonsxdrocokdcsxpbyxdyprsw,vscdoxsxqdyszync,dkvusxq,ybc
voozsxq.droikvvvyyuonkbyexnrsckqo...pspdoox?cshdoox?yuki,drkdgkccmkbi.
ronsnx'duxygrscygxkqo.drolecbewlvonkvyxqklewzibykn.yeddrogsxnygc,nocob
dbyvvonliexnobklbsqrdlveocui.tkcyxgkczboddiceboronsnx'dvsfosxdronocobd
.rodbsondydrsxulkmu...drovkcddrsxqrobowowlobon...droqsbvcaeoojonrscrkx
n."tkcyx,iyeyuki?"crogybopknontokxc,rsusxqlyydc,kxnkpvoomocxyglykbnsxq
tkmuod.robmrymyvkdolbygxrksbgkcmedmryzzikxnexofox,gsdrdrsxcdbkxnclbksn
onnygxdrocsnoc.crogyboxywkuoez,vsuocrogkcdbisxqxyddynbkgkddoxdsyxdyrob
covp;ledsdnsnx'dgybu.crogkccobsyecvizboddi.roboioccoowondymrkxqomyvybv
suokukvosnycmyzo-lbygx,lveo,kxnqboox.tkcyxvodqyyprobrkxn."ew,snyx'd-"s
xdropbyxdypdrolec,kdokmrobcryedon,"kvvbsqrd,mezmkuoc,vscdoxez!"droqeig
kcylfsyecvikmykmr.rsclkcolkvvmkzgkczevvonvygyfobrscrksb,cyiyemyevntecd
coorscloknioioc.rorknkgscziqykdookxnkcyebpkmo,vsuoro'nokdoxcywodrsxqwy
vni.rscleppkbwckxnmrocdzecronkqksxcdklbsqrdybkxqozyvycrsbd.rscxivyxgyb
uyedzkxdckxnxsuocgoboczydvoccgrsdo.kgrscdvorexqpbywrscxomu,kxnkwoqkzry
xogkcmvszzondyrsclovd.rogyevn'fovyyuonzboddicmkbisprorknx'dlooxpsfopyy
djoby.groxrocdyynezsxdrokscvo,yxoypdrocdenoxdcmkvvon,"cdkxnez,mykmrron
qo!""srokbndrkd!"dromykmrcmkxxondrolecpybdroyppoxnob.droxrscoiocpshony
xtkcyx,kxnrsccmygvnoozoxon.ktyvdgoxdnygxtkcyx'cczsxo.rogkccebodromykmr
uxogronsnx'dlovyxqdrobo.rogkcqysxqdymkvvtkcyxyed,nowkxngrkdrogkcnysxqy
xdrolec?kxntkcyxgyevnx'drkfokmveogrkddycki.ledmykmrronqovyyuonkgkikxnm
vokbonrscdrbykd."go'vvkbbsfosxpsfowsxedoc!cdkigsdriyebzkbdxob.nyx'dvyc
oiyebgybucrood.kxnspkxiypiyezbomsyecvsddvomezmkuocmkecokxidbyelvoyxdrs
cdbsz,sgsvvzobcyxkvvicoxniyelkmudymkwzecdrorkbngki."rozsmuonezklkcolkv
vlkdkxnwknovsuorogkcrsddsxqkrywob."""

p_shift = 10  # char position shift for cypher

# 'p' for "position"
p0 = 97  # starting point for ascii chars
for i in range(26):
    p_real = p0 + i
    p_code = p_real + p_shift
    if(p_code > p0 + 25):
        p_code = p_code - 26
    s_code = chr(p_code)
    s_real = chr(p_real)
    code_text = code_text.replace(s_code, s_real.upper())
    # print(s_code,s_real.upper())

print(code_text)
