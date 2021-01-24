import socket, sys

HOST = 'simple-service.ccs.neu.edu'
PORT = 27995
HELLO = "cs3700spring2021 HELLO 001274925"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('1')
try:
  s.connect((HOST, PORT))
except:
  print('BAD')
  sys.exit()

print('Connected')

s.send(HELLO)
data = s.recv(8192)
print(data)

#receive FIND or BYE response
response = s.recv(4096)
response_split = response.split(" ")

if response_split[1] == 'FIND':
  find_symbol = response_split[2]
  resp_str = response_split[3]
  # c = 'g'
  # s = 'duY\\]EPz00a_%upM^KWHdqi#$[?S~{Fa<s"$y@OV@b359_YwPp0__s!MrylJ/lTE3~ZJ4obt8;H@(dS4%kuCP:0yp"(Tj1c_\'B2\\ush;P}.{TK6Kt}AVHvrQ2Z~|)|/Wi1]7I1xBp#*`dm."ss_t9OU~@.URf&C<A,2*MA]U`1WMpjA<._ex!%&La;P"0phvt2^`.Tf7Va4.drf[ax5$J:+>5~AaZ[Jw|P`Eah`VYsjmu=u%"mP1]uO}ce5Zca<bJ0x!7$#!"g`)bO>+4:%kY0^+n\'[+u`kK]-1zt^R\\pC*\\u<SIPOc/#b=KvRi`*EZ\'6p#&\'#ZV[hYfBuNiYO{DlQxMS~H@}[%;E^ybn-cO`VT=iVB1{>-\\o%3?TS@7XA1/\\diR*D;<l#o,Ip*r*zLjLyL).p{I8R<om%_XF=DbEO96[zT.]_H=#U@9`M+?XN3b<I.+kkm-F,zA2RE1]J`u_e"MSo"6D,7]no?v|-Dt"vz4^JI](pi;KO]M8o<Hx[Fu8PfWft^hP8$&1dgSpG\'{"iQxU8*ci:s<2-QP)c>Lm>o><"RBn+l:9"/2{sXIU@AVn.fv1TL\\-TZe]vPs~0^uUIQ\'co?!E8[@DG<:`2@_g$eluCV)6{mBRV7^x7x7bOWy%fPn?4ZDagH0XF*zn+t|\'*!n;Xkm&mUIeF\'zX>Sc%dq`.jf@ZHGG^\\O$wm`cplPM/.o3ij!P^4YLJn)go:oCNC2\\Nt0IzYy>L;z1^n7KNzG\\$|=iCEH80^#dpP/50gF\'UI;VWu\'cwo1mQYVak.<&Z{-&d=2M"+ZZEtY66A\\:yiDjUofs"q+k<!a3Z<>\\(GrR@GvmE2Q&eu6cx?UU8~w_Q\\6>c%c{E*X)lkI,wviLa;wanb[<:hQv6/%~]p,ZDF<F<qL6G\'^fHE=S4^h;:fdQO~\\f^i\\n\\GzM!o:naTB[VT3<8SvCh=\'f@eKuqL%d#OF0V(ITVh<HX!CbX#<BJl"D6"(s+&uF;tLgjw?;6J\\:a3nCXg|E/*e;[p:B1z8/!!NcmS}>(x&gS(fg-n#Q[lY/zWn{PonH1D[r0*4(p:!tP3pmoZ$KtW?P0]>RkT\\7eKyt7\'.+\\|t;))1#Hqqy7iB_2oxI\'@2n{~`l">KCJvGfEfY}=,Y:Pfw4$<%4dgxF:6?K{N(yY40q{z~GU&_jX)Me1D^=yp<JT~zv7cB4uj}m[5Mi0NZNGT0R*R>D\\uTr5@SZ9^mm_@;Q/V*yFxW"&+J[zl{"x&G4!da!Hjy9_Ox(yYPb.$TYyDW9b6(tTL\\`PC?e,_F{02S|E@sDH^Q:JT[_;WzbTK[VrD]|M\\\\_g\\vsPxZ*&9J/O(IAJ@vn<J;O"<xnFShS~zul@@#@=\'$1(y{F;ac9KfNu)/j,8}5iL^qTW%nC;7nDh+$tNyAK"=#%ePu~q/.{-#9B;7qcTc)`{%(TyYqs~[x,>.W_Qdu#_aI)koRuixI+im\'b}](o={Q@=qV.Y!o=/-m?Yuv+S>NP+JA#k"4f6+ek4C}tLqX!cerTYnXuH*\\/f.[/*-UC=W<NIvoT/v@*MD?C/Gh6.,5*u~vg_d*9LId"c<?vebwE\\9n*b&.8wo6ukG24{~qN\\\'~&|q|TUmd\\,H/w|]:T^"bUu0?q`j{eK9?R@4:=d0v9}@h&Q!l2I]NsgP[n-)_=8\'l>6&)*j,?`qM$axjCp4hj>0=NE;2sd^\'XVM#V?lW"*S$%yBO1=]nuN|b\'gpnIC[;BChAI4-S?DWt=lT?\\7LOn"#e4q}@SQfg1SXRiym?8)6dk!5%YZp%LKB(VhC(\'@`VWah7b=z7yeh9b4+B=Glr9V/7:WYj+<(QX:GoTX]Gam*{%eNR70rZ_UnN{W@j}L39I.,Xnw40zRCj;?:OuYX%|xgA&e~#{#8/%Lf%\\;,1VH$,jqe3wfWr]69m]Qpmc]P1V4=S[]QfG_lkb6NR!_7|dW5Svh\'M1PJs)w}kUPQ@8A~Q:t%*">Pp2D/:m=g&KOD\\`J}ti{A~K5lG8pf/Yx\'v5PU8<m{(-jBuRDF_25sMqRs&c>GviD^6JtB"rq8fwxYmNVU<"mN*[.H._D=J@-y@(kcT9lo-h_P8C^(+}QUL*tL.(!rC8A0d4L_lHKg,q0;S3U;ecB,,No]`~.Yj}aR\'^S+N7f7h.]v9m3e:wx$(Hr93E)i|4?G"[s[__LKZ4^)i(ybv<-7-#)JD\'E6lrc#^:tqb0re3Yz)Aw!H6$(08@p!+9[z7;~Q~5\\io+1K?U7}#y,A.E-wt=\\7n1lO!11tALp2jbyNBWZJR;oCbc/KS]nY~hlT5KE,P5vT7amCK)h8~b&E1E&awa"sL4(;ibX0!J\'O8}y[a/@zQ;)P+4:}a*p6DA15>x\\T;{~Vh39unL}*ceO#cC@j)"/NQJfM%bbX8O5JQb!vd`&rfKu+%)ejq#>\\8,~Ml|X^>Run|5_1[ZlZ_;t}]R")[c/Wo~bwP#\\h`!]3S.#`v|&:x*lZpbZ~P%;1|BU>dj%%Gn[I?:-_]9Z(Ccb_P[ZY~W\'V%pZTig^mkA/Bh0Fl`x|.\'CPcDKmv+AmJ?+\'aJI2NFX_!=Z%ZJC#52kwPpoEvlro3y5}~{]Q;pn2#Mlh!4jr*-Sob$]0()v/5@QD/i>-DD7i4[n`wT>3fGB~=EZeA.Y^Owl$Io6[ELV5,1y2D"?rrjz*>RdmKTlJ,mHiO+u9"\\nkXb2p{f)J^|p*O_Nv="sA{IZ#>Rq=w@v8fqUI+/h)Tit/CKU,^|_V0&rX=jXYe48swT&JcWkWnj7n@a4q+@p5Ru0a),AIva+`!!zqTiY/+A8hz[z+}CqC\'ExmLm:eU|W2OoIE!+\\@TwJ!RpNQ(@fZ"Rs}H]!2KEnxTN:{~Gp@~lWLlZeKe+LbUz?Y_7?:O>`Ldih0zK1[^\'wAp6BB1>:;&D=rQ@.;C%[D"1hlPW4c70"\'J9qW];URx+$,At+sVhLR%W#uK9n+YK|0[);AL5qr%m=>hc\\\'b1^\'D#}N?xV6d$_`+[Q5@zO+[2dT3&k@5b\\nk*|mZ}]I4ZDPBm+@0xRdA>J*+M+,kRUbp*7@Oa6S+dnnT<;@$c<g57jf>\'Z!zy\'m0XdI)`jUKRx&TV)KArJ\'4A<;%3AmG=z&p^5;J~BzOKl7ATn:LzHR=Cp0["q9*MW6#\\x*"$Z,#sG#zi[N44v@8Q51SM&0=>*ArK#*5IeTd1xKLRifPL!\'0E9Q~@jpJXTs`wcuFGi))dH\';GbSz|^7vkvLaWz4/Q_[jYW<"Q\\;D9qoY{-F-mW2\'[|n^02uDN?LpzlbmY$v~l3)s`nI8VQ,Yr"zA(sXO?XP$v<4IIgo*HTG2Y>K;9g$Jxc4"h\'K~\\5BqwK4e<P~o__{J^`?mZC/O|Qy4saC0k\\FoG{MP?h]f,abMtfQWFIfQC-kt!cG8sL~<,Qk]NAh\'#C!Rf40+rBQKR=u*>X]a*,x2:`u`6Qh({LWjCO5awt<Y(uM4$M8?Z\\{T.X}A)e*}JmV!?rYk5xX%ep\\!X|f_ncE17\'Db&tz5W*!tY$#XG^2a]`O;y5S+Hoj=:XvHW}=(|}vm^t)G,@I`-Sd?&EHp~JrpI@k3:JT,Z#CGJ|`Ds<Q!yFOR&BUq7#BmiFe|-~gGkAku54E1-OuohQB`y+&nI`D^L:m]zID)q82!1l83=JlKjV|X:6l%_vUwNfhGG&&nHm&d}sN=Ibf@t%xb$@3\\Ksxq;1kIU;1<e%a7[Qv!;pW^62U,I\\bLJI4I6S4Z[G\'g!J>k}*Jl]MMoPRo@Cc`rWDtX8,SZ3\\_RfZYO@26`gH1%6G<<Jq<<|[\'MyNJ"F4;zs0z\'A>~U==qZzx!7rOw$7/Le0og|A:2gF\\1?R60r\'z;vhHJAtn?%XSj#jp+_/T0H8t[6f;_>`0yozC`|r5-Xs|c4:_1c+3DNUHj>Bb[)UfUD&Z9LB\\FAwanmzS#^#X28a3Q"Q2Rn4p!E9"anG#A^+n0,AvfbqH+os5kG+I5($\'|kj%)$:7ML5O52195U}!+o.JKVRj-sb;`qOt1`JfAp*|SE{vxk!X.=cc%\\^pvK)if\'P(&-|=1Eiym2]1Aqt>OYI_Zzl~]Q7;;QPcr?;]8)sMR[CbQ|-gkJc:O"tOha3Q+KOZ.'
  count = 0
  for i in s:
    if i == c:
      count += 1
  print(count)
else:
  print("BYE")