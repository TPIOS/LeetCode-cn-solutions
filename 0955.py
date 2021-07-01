import copy
class Solution:
    def haveNotSet(self, strs):
        n = len(strs)
        for i in range(0, n-1):
            if strs[i+1] < strs[i]:
                return True
        return False
    def minDeletionSize(self, strs):
        ans = 0
        strLength = len(strs[0])
        n = len(strs)
        tempStr = ["" for i in range(n)]
        current = ["" for i in range(n)]
        for i in range(strLength):
            for j in range(n):
                current[j] += strs[j][i]
            if self.haveNotSet(current):
                ans += 1
                print(i)
                current = copy.deepcopy(tempStr)
            else:
                tempStr = copy.deepcopy(current)
        # print(current)
        return ans

a = Solution()
print(a.minDeletionSize(strs = ["vvxejcrulnxamfxbkqlnpiahmbuvltqjqtwocaxapyicraeufsoppnvgjzviemxjurvmqgudlzhgupsvsxzzfgfkkrdalgnqommw","lqakiuozyiuuyjfbjsfkbttmrnctgexxsizfraxfspvffrfsangdsbueyqfpkpqieqaafhbaocbzajmnidtnwqgkprixqzdfblwp","majviidklyhfrixjwdhkbwoyuoldrttduhfokariaeqwgyzscjoibzbhsjtfcefzlwnskmzltizvbigduavvkvfjohjbcslgvwcy","ddichavlcenxkpnbqkiewybdkmsafrnsbtnovatldrxlqcvgmeawusyflznkjbdablvvlbotyzydzbpouwbxotvbrpssoafyaran","mevbayyazaqbxlnogwzzzsfrziuyrzinangdearuztvhscqdotorjdaoempuzrydtmgylzkcfcdhtuovsueuyfmjdyyqaevempxv","swxumgueqqyztrcstcpsziirmqeugrndptzdfaovvvcomhljsvpoghfhcxnzetmruxrhmvvpljewvojhuztzjesommrnwhvgwrcf","oouxsczlswqduchqbexhcammderstuxjludxgalvdyvozzjlrkdvciahtmoqiofieftsaioawvswqqvijnamrbbanxpgffixzvkv","bcxmaudsiwrfcetjotmjbxrzxeuterckvcdcqbncdpyybqpuibptfwaaeyglghhpynyagjayiryyzugkscxlhctekocopsqfibai","dmtjaomvcvtmcmyprrpkthotiouicaiigrmarcbgwpgkaxfgogskgilastwjyrkwlbqtntnxgkvfpfdypkxbrseiriqtnwqteooa","xrkvkjseixbgjfbbeswzygmncfriynnjbfthucsjtbkhsiehqmchcfqzjpqajnfdxbpeaawtjukuaadunhdxtwjeyzlibxanlgtt","dcbzjujzdtfrzvmectlxxnzrbrjeoajfqnmxhcvltpcltpawljpmjtdwtfarmgwbhybzljmboopukijtyxjpptgfkexhohrmpldf","xeasfysgofkerpfvhufzmcssnprkpwfnbqxypcmsroeeesfcocbrkacqkuimbfoooiyczxlkmptfiocbwbjpkgihawrufyovgxsu","tnnvfwbuavaifeieajrnvgwpiphxwwapweonmcdyxccirwdlqpngvckdduhuosomoekppxoksilhvmpdhpmajtpxvipeenmkkafd","kjsnbzgyzozlfsxswyllbesjggiiicicnjadecgzgwddmfdrlyayuhmmuuugcnkbotxlrcedjnmlrkikxsjqqgejqkdglkazvjic","syxvebchdqgxrqfdgepzkwalatgdmopigdvyhdkgkoenrjyjojrnouysjfzbzhluavvvzgigcyprbttdbdmvwunjzcmokicbmwig","jobdhujosadevfjpvjblhkrtwrcgigbhadteadbkuubveqjqktmnetrqqztjkajjzgwfxtuzttdxqffwnltynwxmthzndzweyack","sjlvidfovhreachpjlohhfiwhckivfnzkycmzdbljbqsgieohgcmfpugyoyiuvrrnmlbwedkkiomtahiunkxbydwhgnrpaqocvha","yuuobhxdqkefwsztcrsutpqrrqdtgcivycorydzsirphcoltyffxxiwvykyvhgheuabmujfgystnxecahzcxeeqleuqnpejtlrtb","odoqphvufxglfojqhdhagryhlrdlphcrvrlxmeenusjojhayyuryjbqjimpbrskniqpozpwxvnxzzawjxaidfunanyfnpkuqvgcg","tnedwjomyuwgyuonaswjlvwnoytgbmawavdjaewzsgxgrvqlzyojbxtloxxqggpleawbetmnqmtqwvfvittukpegmccdvbfijvwc","tmtmjvrbdkerpukrcumpctmmxzoejxmpuepkuftnmieoieesueulddkchrrnovtxoqtubxwqossmwyvgsrgqansjdqcbvftahhgn","rttugtufedysqbxcshtnpsrcdgiqiqqoqdlhxgkdektndvvrrpizdysvxwcsmsvrhawowloiumbacceurroxbzugcqqwdwseiqcg","nlrbahdkkzhlbjxaevpdfbxpfzklvheggwxsmgnjgnopqrmgdvhemsgaffrfyogcyfqqtzyuasmlfzhxlrpuvhypoggytwzbkdak","pfsqgoawrzmtppneapcmacwsrfxfxnxgbsznygloeshnfftsnnirispfgsnnmdbwknjkslqrbzswjowsufnunazstbgggmjjaaal","dbzwiiikwpxdamatqayeqtovwqbncnhuvujcdhcahpazjbuavofknubgkkezaiuvkyxbqihpszfvidrpolmtzfpdbubngeufukze","hiutwttchtsxstfmonvrmfswlqhtkcelwrkxlhmkotjjazdlryuxbnerlxbegtsfyweilekuqqnuyzkljtjsajisdlficxpyodac","oidzdupsecdfawqbyofdwglamhtveotbrwguzhhtafdxqugpibjlgfcykeinoyeddeuzbsuaovzvcyagbgqwpnqjurrmgucxxvzr","ttfequhoomcbckhriplkrjldjjgbuosozsxhdidapwgmiztbjriycuzhtwbablrvegmntvihpxwvtohcqmrpbpdeofexcffyisbs","rxdrwsuixnvxwxxvxqdamenqsmjqakulfajsxiicpaifpqykqfiqtqumjkmegszbxmrjfajxohkvbxntzjnkgqutuhgwkazdqcdo","qtmawynhcbfvmkmfejmrwfforuetbotadjxhhiahwysegxklkssgmgpjyjzivlxzhybjvpoxdzcyqsdtjfcniqwrjbeveamhfrun","fbujppkgzjxpkzezgsmrvbrwtarwyhtwbiyoziklmefyptiapavsnwcfilgcnobxtykhdqbabagvloxmjwpoqfhxkxtruklzliaj","lvsxjycvwztduyyiiemkfnbezdirrnpwellteitnwaoctlihcxsxbnydicytcltfewazeyvbbsyztsdmyjkfmbeanovqtgojmpfi","lhlpqymecsqtctvidukotjbdlpfxfvoedfgmrirqndvaehyxexnbypoeugbuuwtvvbziulwbqlbylljehaxmhvwyvbatccmglhmv","jjzradoxekdczywpwepqpcafjoiffjtulxqlsikulgmevkjlypwbedxrfmjltlrqzsrzxlwmtfculzsomxrehgbkrmamrisxpwfp","yspowyvusaurikqpoixlzqmiabhgkvszveuxrjxcondwnihowwtffrmcthdnksepcspmteignoxhmetkddmndtmgytqjdmepfhfi","csctrlhcvsshxiipwmduhnrkiupqszquwdwxbjnouzreyjyqeljbsekdunzmhfgnjvvhojevgoynwpxvlsilcrbtisdynbjwdmov","jlhaprojrzbhhtotkhdfqkspiubdnzomurdbrkkdwrstpexaligmjfmjyftuwhkqeludlutrrndsmsbylbmpdvikmombgpdpgwij","bjbvltxijnsihgjurnwfgywgrebqnxuitzqvdkzootvmjhwzotqfyxepypfdvykzwidscykpmafucybkqnkvmgwqjrfzzixagdoe","xtfcxgazxutdbazevijusdnkabhnkxypibfujldakzuhgzgneqwpumowqhirpqvmnmvxeeuixuoqrywjatlagqmccpylzwcogppd","gykduitgbuxizbmdluoqzjspgrudcihhdfkvolpdbaodqxmdradsvbxzpqobwijvbtdaauvhxmyzogzesmxjjtuyclznvrtjvvjo","nkbpmqmghhqlrhwnfgopfiubugrumefwlqqrzlwiseclgiqzkoqfljqfjqfqsvlmxdkhdfndtgvmuxpbfwdzkasverryenzfqxwi","vwdhcgxazszewfahphcgaruzjmswzvrrtuqoxluibgmaziifyceelkcpgemlciewmvewcpgoqxueiyrysjrpiepkqcmnbkehdorn","gnqqyxsnoacdqafifihlvgymormytbqvcklydlcrcwbeuinvecndshiaothpobikbdhxpujyqxaipkkyrxfanwxykpgayexfexzf","pqbhqleuzhznwedawihmkqsibsshslbmrecvpmxbynqlbhcsaclbixbphfndiaepuqchgfxpoxvvfopjmiwevfsjtjynlpjbchve","uyxrklfqbbbpdclgblgkevrqgmmvwpuxqeqhymkcnvikfpcukuznocokolqegtchtzcboebircudlmlguyceqdtfeveovxoppsex","jfqhlqkrlgyitnwzcfofkmmzqduraaxydaafdmeorhmalzxdaakrlfemruoxqyaaluwodznukscrnnsxlnhocgollnfbunnkmcvs","fimpptwphjomdoehcpovclnoshpufjscxcjbsmcusxjilgikoqqqjrmynxmrdlijvkwdkolpieurtyvxomdkzfsrgtrgjjxcctup","nldvamkchsjbpqecawtqocstjoiuhiesvxkeomovazwheycwrrhaofsesgkiiislzefleabsqfpspdwkdxvddrrffqrcmcxijtkb","euyxnjjezrloluwwngnpstoqubtlatkcotkvhncajvaeinpqnzozglctrvwvkbpygsjbtnyyyrbnkjlqkxhciuzglilyxnihjhjm","aiesxbgplcbtumyxurccirxsufuleardkvjppnsljfknqqiordouqxysneqcpcymppjrsidyjwzizxljjxpbmuhtrwbxsclfdqwm","rmtfualnxcjnsrsrwtxknyzoqxejeqcglwzmjnbsgrlefrgrletnucutlmfcteyvzbiglpmzviyhyqazvhulxtqqlnqlfwmcuxxy","awrxgheeaoszkfddwadtohjqfayvgafqmcovlnpshydzfecfhazmhqhzyjldwljpiesdtfywijnninczrctinrvnbckazagjaaqe","oiwkfjyozyhsirieidacsdzdaojdikpfdydjbnaxvelruqaouhifvvqfcjjkdmrrfrpdtxyapannqicvkwvvgalzqxgouoajfpzn","lsmzdlwfbvwathgnscdgaltlqafumdukvarclogejgozolampqewjglziaveeiszgemfssiquhcuqkhjelrwkygcccbzdzyqtloo","fdtxqknyrsanwjwdkcsojtsbjvkmacrsqvsirojghqgegnvliyxhqdmescoyvzvahdfhogjcyppkdwekhdhsjfejaocclmfjogzw","xvbutyybaqhvetstybermemdanmsjsnfkhibkoauyphnwggncyrlicryfhsxehxrcqlnbfcyvyjopotalqevayptkzxpwunwvrba","rmjjkhpgdlmfepsbvsdfwuoeiajqoelxkleapogwxmnyrqefblxiznwchridsphoyudlypcxyakmzgottlpartkgkrmmwnmzvglz","egvamcvftjfdhabkkyldlbvvupwxflgmcjipgpdgfthxatoqgfvfizsiacjiymcwmsefguxhkpmpyijxekjbnfuonhkuolvfabus","jcysacpeljlcnnmlaxnzjtadwphppngexewlcpnowbltcdwwxzgpqnkogfgfslqfycetghgchveecjrmrxpjghovhsgxckkxzkyc","akyndnocnvrbizjplcswjyyapnpmzwuhmubqnpkzfldhzazkmkbiwlnokjsispxyzclnxkxsvfegygnqnfpqjbjeedxrlejefgqu","ljpnsefnaxgntothoyoexdipzmujbaispfdjaqcbqgjsedyadgjlvokyyvnmjyvdklkrlixsdvhfedbtussgottmgmmgnfgsuzkr","dfahrhmtrnmdsckcswccctmjbaxsgorcqvqjsqaguesljphonqoyjwfpbxlfcvcxptuumxdfhyrvlxjlewvwnmbvsdreswvdazeg","pyhemaflwmgwdpntkiaxoankebqpsaajelyrkqxlrfnvwdaecstieumnhisyavdmjhykxdswlclikmcxjpycnttepqlxgmapfsyk","bskiaplfbfopgeledgbtnhjugwnqkubdftswcqrpnpaojwipwghfmaxxvgqrbgkiamhklmpqlshbuwrahiuicimgtquezvtdieju","dajfjqqeqonwyvuyostjlyksuqmgdqorptvqoqquijccopxsewwwxxktwuaiqpbenszqzmvrxvbqkmxidbqnwoxjpzelbnqwhjuh","mjaqekpjoetibplniwilxiiexrljgicgmkkueqouptkvbhlzdlfbtcbdsfmzqzanszwktvoniazplvkxbdfpxsiubrgxpobdsfta","zfkqgakxkjhcirvvhwrhinaybrymxdqtleqqlrhayaxqehgqihbcdidwozrgdpaezpzcvmbtgpennwrftagsbxcnrtzvriauokmi","jdbxxhdirtrrruotajmvzaiwpvsbndrnywzbsrzbkkdvybketfvaltfazlvppsbbcbzjzskictpshyrztnnqnlvcxlmauujbpawc","zkbbxpufdgijsziubgysvtghzgfjzylfwhnigrrertqptsoormkhajtlmuzlbukgwsnigurlzovmtihyfroiasrpqsvbiswashge","nlxvrmpgsdbkplnprypkrvfvuvwlnmpmtqsrirlpahzjxawbahrkehbcbeorefhdhfmndtcshceoovmchkjuzygqyqbpvibiueju","tqkckzvcawhgbwafeueqdokidutnzoblajwqlstmfaoumjfaqsqzfbzgwnwdrwjfvgulzwsughjpazwgjofslnrajoetxxpcdhvm","nfkquuxgsqgtpaoqqmvzhkvehsdeoghgukmpdszszwneohxzelgnmqfqlkwxerlxnojiblbnigfawxwxidlzzhomcrbvvdhhgisc","gqdeibxktuaqdheoegcidmqdkvddwhckwdjoxtsgrdnfvboqdxalekkqbvwjnfwswjmddnppqgarnhaofrweinsfybfcmgelrvkq","jljgahkwfqwofzgmvhjarqrqpordhumrawqchtshdocsrzjlugnlflzhdqkizvhcheppgxzujiockxghvbhmpwqgqkhglcfjmyuh","ajoyvegffjencywgixdmbkvfflvhjyvwynrwmtzkzkdncppzicvahvueygwnzhovbfxvqehxufbppwgrlsivokozbouhyojwbhwb","iekpdgmeaihgkvvxobkwoapvomuobqytcywkqtcmpphaevnhvgzqxillcanxzzuszfcemdzhdrnktkfljduzxoviqpucqeejyzor","cbhonhiqdjyisbnyvixhmgbhmwpakzyeqsfwcthpnecitkmzhtjqmfzimlkyqxraxotmrolyeciwysmyopzxrdlifzpbfyvgpmps","bqqnpzynrwlinhydagfkpmblccjlqymmpzytetrqbrwwkcmofbytcvephmplyjuoyqluflqoexgbrstksxcezkrkfofppuyyjmrd","xinequgxdwrjcanssohvbakrkaoahgdnfuprhumdyjtigkfafbhzohpgiwbiggoueqribgwnmfzsdjygdaqgpdnghejvqyerhtcn","daxnbubhbvicqiotyscvprrmwrcirkatsymwsuddszdmcwobdtonvppphmyhisduwicerndyrmviugmjmsecqfjfuilitbprekpb","fxkpfnwvshjhbsjrdpaarwvoyxubpzatxevbxubgdteqaovhphsohvnrwhjgrfyrlgdciqkskvalxfzeqkiokvzqfiqwzeygqklz","youflzgvieowuzcljmqxwstpibfqkynsxljscuyltpppcvfbslcqocxuyztickgnyexgqyravovkykpscvzyhfdwjtdyyleejfav","wkmzqnkvlxrzjnjlvnnqlpydvvyavzhaylfjjurpogexwfipzetvewqagsltqugadpsfalwyhhcxstyqpeddrszjyuqvkjmrmcfr","pnmreilozjohbhgentgtrsowcmoxcfwpxazygvqeocxiapqsxzyctlebqmhwqxpnpnorksiqmlwbgzuaxxmtyelmxihnmtwqexvh","mgrjsweqfamcsrcxkplgyxivnhleovcqdznyfvnfqhtpxdbutfocffgdoplvntuixroinocjkhurwywnoocqceseettdaidkfpgk","kstvfondsurxhxhtuiooyrbzknrkcpcxzwdzrveikjyyaazidyuaniohwejiacnekknhkbwhkrmtwwowrgbwmncaikafkadizmtg","nhgxqrasosotxncapimdjiyllndiaflwqublvvnkqkjdmckidcygyhwbjwmoutzhyllumsapjenpmkqywtitfywsleeaqcfcyazh","oyzmysmwmkvphyoxzvqtjmaykkmdmtqxlfpjgvklsnvanyxvhoxzpuuxyeeubozejyxbibxdfcfzvqmtxmyxgxquaouiucehxvgn","hakggvicoivhvgxoesqwjkrepbfplkwfurturwbbejtpozgxttnnkipguegbesvdhglhpfhibqhoqtxgwdgqjdfirmcukvdgswjy","kfdhfecozbxxwynqntdwapxhsxnkzjcuotriuwwdgnoinqeohkmxctrcygqppdjuotwvayefbglmvggbqhsyonasdkibofxaekhk","zdanrjtgzjqrmmdvpgiaayjzmonbtuqdojiwcwrfncciemecubruaxxfwuqqvuflprqqyybhllelghixpkuubmzwcpdyjglryeoz","nyfwepwfcmgtkfmuwnkrsdwwwrxvgjhwkihiixrbagjjkkysyiiubtapzpascckcngqygqkaovzkjleqhguxwgexskydpupehhln","yousfqsojqtyeoirmrjzfehlehpmoxyprkiduxsgxcgaddoqxstyarcavfappojjpsxxivcrdzpofitzunfjdmidumnnkcnxczcs","wazcovqsnqizkwvbufknrzfiyaufckaifuclgxeljhhjfizfieopshkwmnrceegdamnfewooecnomggcsmciynypkkcqxezjyjbl","yrryieqyeefiubgywiugmhlwcecyisevwawsexystbsikfjbwzgljdpldorogwyvcoqreqhloaqiogbanukrhmccbubuvzgvafqr","gtnbojfqcnyhcodzzvrerqcwaogevcczrstelxssrqabvqnqglwuqgjwqgjxjvojisrhtrjogumpojtlnxbgznjftwacshuutzyq","oovyqqzzxreckjykwwkhippffulmjjowauswcxutmujujibyfrxwabfjbyhjkxzlotaecsyziyytxebtinmwcwxgdvbzrbiquwag","jzigqkybsssewtjmmeheiwccfweiufeqgeqrnxvyjzxhacxjccxefyjkuftkiaablvtdwivtfpkovprbripodntdlclxdntwkayv","jqskcwpdcpunmncsynowjifmhdpzosehgbbdbypveqqczdptqbagrfhunclqpehwhdaujkamecpykuabvajpevysrpkiztasdtsr","hgludaxhhjdagglsjudkefuoilctomlfldxxwzptbsmqcealippibzydfokzddfaxbcczgwxkkbrzbgqptwfgagvlniuqqagrcen"]))