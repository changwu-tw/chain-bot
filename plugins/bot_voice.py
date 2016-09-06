#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

url = 'http://vois3.cyberon.com.tw/cloud_tts/gen_tts_file.php'

data = {'outfmt': 'mp3', 'speed': 1.50, 'gain': 1.00, 'f0': 1.00, 'vbr_quality': 1,
        'punctuDuration': {"，": 0.5, '。': 1}, 'language': 'zh-TW', 'speaker': 'DaiYu',
        'esl_speaker': 'DaiYu', 'esl_prosody': 'Zero', 'esl_speed': 1.00, 'esl_gain': 1.00, 'esl_f0': 1.10}

headers = {'Content-Type': 'application/x-www-form-urlencoded',
           'Referer': 'http://vois3.cyberon.com.tw/cloud_tts/pc_tts.php'}


def post(text):
    data['text'] = text
    r = requests.post(url, data=data, headers=headers)
    if r.status_code == requests.codes.ok:
        ret = r.json()
        print ret['note']


if __name__ == '__main__':
    text = """
台灣金管會對金融科技發展的願景應該如何落實？
於台灣新舊政府交接之際，台灣金管會發表了《金融科技發展策略白皮書》，總結了自2015年9月成立金融科技辦公室以來對未來金融科技發展策略的願景與目標。這是中華民國金融發展史的一項創舉，也增加了台灣發展金融科技創新的信心。金融是最重視業務持續性的行業之一，金融監管政策的延續性更是重中之重。然而延續並非因循，金融其實是一個需要透過創新「不斷革命」的行業，產品與服務必須要配合市場與客戶快速變化，監管的思維與原則亦需穩健又富有彈性，方能與時俱進。

為了持續提升公眾對金融科技議題的關注，我特別訪問了FinTech Taiwan的發起人臧正運博士，請他從亞太區金融科技治理與行業發展的諸多面向簡單評析這份白皮書。FinTech Taiwan是一個關注數位金融創新的網絡社群，結合了一批在法律、金融、科技等領域富有國際與跨界經驗的專家，長期關注全球金融法規政策的設計思路、制訂過程與實施成效，冀能促進台灣金融科技創新環境的持續演進。以下是此次訪談的摘要：

Q：這份白皮書最令你眼睛一亮的特點？

A：白皮書開宗明義表示：「本白皮書規劃以2020年為期，提出『創新數位科技，打造智慧金融』之願景，推動資通訊業與金融業跨業合作，達成充分運用資通訊科技，打造智慧金融機構，創新數位便民服務，強化虛擬風險控管的發展藍圖。」這是一個大願景，不僅是政府內跨部會協調，還包含跨產業監理思維與法規調適的各種議題，後面要落實推動的工作非常多。傳統金融監理雖然亦需要高度的跨業監理協調與整合，但其層面多在於同屬金融產業內的多種不同分業間的監理整合。雖然在產金不必分離的時代或市場中，金融監管者亦有跨產業監理之任務，但仍不若金融科技發展下，由於金融服務的提供者除了以銀行為首之外，亦有可能以電信運營商或其他科技業者為主體，故而產生的高強度與密度的跨產業監理整合需求來得重要。金管會金融科技發展策略白皮書是一份綱領，相信後面陸續會有執行面的建議出爐。

金融科技的發展浪潮除了帶來交易型態、商業模式以及產業地貌的改變外，也將衝擊傳統金融監理的理論與實踐，進一步將金融監理推向新的境界；我們所熟悉的監理思維必須有相應的改變，始能因應在此巨浪推動下所將遭遇的各種監理挑戰。

白皮書最讓我注意的是關於「法規委外管理」的討論。白皮書認為，當更多法規遵循和監視流程集中委外，這些外包公司可以變成監督機構聯繫溝通的控制點，透過自動化及高規格的法令遵循，可提升依循法令之速度及效率，讓監理機關易於一致化管理，也能改善現行法規解釋太過模糊的問題。 用職業運動來類比，這其實是類似「專業裁判團」的概念。國外有許多專業金融法律遵循的諮詢公司，許多任職的顧問都曾在相關監管部門服務過，對監管邏輯與政策意圖較能掌握，又因爲在金融業界工作，了解業者實際碰到的問題，除了定期針對監管要求協助業者遵法之外，亦能將實務上的問題與需求及時反饋給監管機關，是維繫與提升行業標準的關鍵職能。金管會提出這個新穎的見解，或許能催生台灣新的金融服務業態。

央行用區塊鏈技術發行數位貨幣是否會影響金融體系創造信用的能力？
金融科技的發展浪潮除了帶來交易型態、商業模式以及產業地貌的改變外，也將衝擊傳統金融監理的理論與實踐，進一步將金融監理推向新的境界。

Q：這份白皮書所體現的新思維還有哪幾個面向值得注意？

A：白皮書對法遵科技（RegTech）多有著墨，對提升台灣金融監管的綜合素質提出許多指引。法遵科技不只是「廣泛蒐集各國金融監理制度與法規要求，提供分析與管理的工具，能自動協助金融機構遵守法規要求」，更可以進一步協助金融監管者有效地針對個別金融機構就各類監管指標的合規程度進行即時與自動化之監控，將是國際上非常重要的趨勢。期盼看到更多金管會於未來將如何運用法遵科技協助其進行監理的想像與規劃。

另外，白皮書中關於建立金融資安資訊分享與分析中心（Financial Information Sharing and Analysis Center， F-ISAC）的建議，很值得推崇，這樣一個連接各業別之金融機構的資訊分享中心或可考慮導入認許區塊鏈與智能合約作為該中心的基礎設施，並進一步將之建構為針對金融業整體的資訊分析、資安警示與系統性風險即時預警的金融監理儀表板。

白皮書建議在短期內「開放金控體系下設立「身分認證中心」，讓各子公司可透過相互認證，為客戶建立單一登入機制」，而長期則研議建立身分識別服務中心，由公正專業之第三方機構，提供各類身分識別工具與識別機制之服務，以API介接內政部自然人憑證管理中心、臺灣網路認證憑證中心、各金融機構、及其他可提供身分識別資料之諮詢單位，並協助發展各式身分識別技術。此構想可以透過區塊鏈技術加以實踐，並有效提升資訊安全。這將是金融監理的創舉與核心。

金融監理中消費者保障與洗錢防制的兩大核心任務，通常需要透過金融業者嚴格遵守並執行認識客戶（KYC ）的作業程序方能具體實踐，而KYC也是金融業者評估客戶風險承受能力以及實現風險管控的重中之重。傳統的KYC透過業者與客戶間的『真實人際互動』來達成，而金融科技服務下的客戶身份核實、信用紀錄與償債能力查核以及風險取向等，則必須透過『數位方式的互動』方能實踐；因此KYC將變成KYDC（Know Your Digital Customer/認識你的數位客戶），其成敗關鍵將在於金融業者對其客戶乃至潛在客戶之包含消費行為模式在內的各種數據資料蒐集及有效分析的能力，而非單純的臨櫃問答或問卷式的資料蒐集。

一旦身份識別工具與機制之單一集中化服務發展起來，未來亦可考慮建構一套數位身份法制與監理框架（Legal and Regulatory Framework for Digital Identity），釐清因此一身份識別服務所衍生的各種潛在法律爭議。這也是一個與數位人權息息相關的根本議題。

Q：白皮書提到要成立法規調適會議，你認為在執行上需要克服哪些困難？

A：金融科技法規調適會議的想法非常值得嘉許且有其必要，但除了法規之外，「監理思維」同樣需要進行調適與創新。監理思維與範式的重省與創新，是臺灣打造金融科技生態圈的首要任務，也是金融業轉型成功與否之關鍵，更是協助臺灣成為亞洲金融科技重鎮與監理典範的重要推手。廣泛參考全球其他市場的經驗，會非常有幫助。

目前全球金融科技的監理邏輯（或稱之為監理目的）大抵可以依據不同金融市場的發展程度區分為三個主要板塊：

1.以歐美、英國、澳洲、新加坡、香港等地為例的高度開發市場，其監理以追求『公平市場與金融穩定』為主，以鼓勵『盡責創新』(Responsible Innovation)為輔，並圖兼顧兩者之平衡。由於經濟與金融市場發達，網路與手機等資訊基礎設施高度普及，且金融業所佈建的服務網絡綿密複雜，金融科技於此類市場的發展更多著重在如何透過科技來優化金融服務的提供以及強化金融業的風險與內控管理。而監理機關對金融科技的監管，則更在意是否製造或傳遞系統性風險，以及業者的行為是否符合既有法令與監理舉措的規定，而不會對市場秩序造成負面影響。

2.以肯亞、菲律賓、非洲及南太平洋島國等為代表之中低度開發市場，其監理係以『實踐普惠金融』為目的。由於這些地區銀行家數、分行乃至於ATM等數量都極為稀缺且分配不均，但持有手機的人口卻不少，所以在監理方面，更強調如何利用科技（尤其是手機）來提供不受地理疆界限制的支付服務，讓每個人都有使用金融服務、接近金融資源的機會，以達成所謂的普惠金融（Financial Inclusion）願景。在這種思維之下，鼓勵業者創新、提高消費者的使用意願及頻率、保障消費者權益等（而非防範系統性風險），就成為監管者最主要的目標。

3. 以中國大陸為首，正值經濟發展轉型階段，而仍處於深度金融抑制（Financial Repression）狀態的高度開發中市場，其監理則更多以「促進信用公平分配」及「減少監管套利」為目的。監理之重點通常在以下兩個目標間取得平衡：「鼓勵金融創新，進而降低民營中小企業與民眾的資金取得成本，以緩解信用分配不均」以及「避免市場脫序、減少不當之監管套利行為並實踐消費者保障」。

台灣的處境，非常特別。一方面有非常好的資通科技基礎設施，一方面又因爲overbanking而導致本土金融競爭環境一片紅（血）海。因此我們看到金管會目前就金融科技的監理，除了鼓勵創新外，更大一部分是希望能確保金融機構在這個浪潮下能受到最小程度的負面影響。 背後的邏輯是將金融科技的新創產業納入現有以金融機構為首的金融服務提供體系，而非鼓勵新創業者顛覆現有的金融服務地貌。

可是另一方面，若站在尋找臺灣長期競爭利基的角度著眼，如果能夠發揮臺灣既有的科技優勢並善用民間創新力量，或許金融科技能成為一個帶領台灣走出悶經濟的突破口，增加更多就業機會。此外，如何透過金融科技的發展，讓偏鄉的居民能夠接近並享用金融資源，也是監管者需要持續費心的問題。

所以對台灣的金融監管者來說，這真是不容易達成的微妙平衡。一方面要確保金融機構不受過度衝擊，另一方面又要觸發創新、引爆經濟成長的新動能，還要掌控並因應對岸來勢洶洶的金融創新競爭，難為之處可以想見。

白皮書強調應「督促各公會參酌國內外新興金融科技相關管理規範或標準，研訂自律規範及管控措施，供金融業者遵循。」其實基於金融科技的跨產業（甚至是突破產業界線的）本質，促進整體生態圈永續發展所須之自律標準未必適合由各個產業公會自行提出或研訂，此作法或有可能產生各個產業因本位主義以及各自利益無法協調而生的緊張關係。

另一個可行的思考，是由金管會持續深化金融科技辦公室在金融科技生態圈發展之角色，或可某程度師法美國CFPB的『Project Catalyst』以及英國FCA『Project Innovate』的做法，考慮讓個別新創業者可以直接就其擬推展的新產品或服務尋求金管會金融科技辦公室的行政指導，以及法令遵循的指引，讓金融科技辦公室成為跨部會的樞紐，亦朝著成為金融科技監理服務的雲端平台（Regulation-as-a-Service）而演進。

Q：白皮書的不足之處？

A：白皮書列出許多施政目標與策略，但並未特別分析現行之法規與監理措施對於白皮書所設定目標之達成有何正面或負面的影響，亦未能針對目前法規與監管所可能造成的限制或障礙提出分析與解決之道，比較可惜。當然，白皮書旨在勾勒出台灣發展金融科技產業的願景與方針，對於細節的法規與監理議題著墨較少，是可以理解的。在未來，我們樂見金管會對金融科技產業的監理途徑選擇與監管思維，有更多新穎而大膽的發揮。

臺灣在金融科技的發展上，勢必須同時兼顧「鼓勵金融創新」、「穩定金融體系」、「增進金融資源的普及性及公平性」等多重監理目的之平衡；但這也同時代表，也許臺灣能在金融業與金融科技新創業間建立一個正向且特殊的「互動共生」模式，結合這兩大族群的能量與智慧，共同推動並實踐典範移轉與金融服務轉型，相信這也是金管會一直以來努力的目標。

一個值得參考的具體作法，是採取結合協作式與迭代創新式的監理途徑，在一個風險規模已辨識可控的模擬環境下，讓業者盡情測試創新的產品、服務乃至於商業模式，並與監管者高度互動、密切協作，共同解決在測試過程中所發現或產生的監理與法制面議題。這樣的過程可以稱之為「監理沙盒」（Regulatory Sandbox），也是目前英國的FCA為了因應破壞式創新金融服務的興起，而正大力推動的新監理模式，非常值得借鏡，白皮書中也有相關的介紹，而長遠來看，更可考慮將監理沙盒發展成為一個讓公、民部門的各種利害關係團體代表間（監理機關、金融業者、金融科技業者、學者專家、消費者以及相關倡議團體）充分合作，共同制定與實踐金融科技監理標準（甚至是法遵科技的應用標準）的協作式標準制訂程序（Collaborative Standards-Setting Process）。

白皮書亦有必要深入探討跨國監理的複雜問題。金融業是高度全球化的產業，全球金融市場的互動與連結極為緊密複雜。傳統的跨國監理議題大都環繞金融機構的跨國經營所產生的相關監理協調需求。在金融科技的發展下，網路的無疆界特性導致了金融服務本身可以輕易的穿越國界，舉凡比特幣的交易與使用、網路眾籌，乃至於P2P網路借貸等，只要法律不予設限，這些金融產品與服務的使用及提供完全可以不受國界或地理疆域的限制，這勢必將為跨國監理帶來全新的挑戰，台灣必須在海峽兩岸與亞太區跨境金融監理方面，更主動地與對口單位及國際組織進行更密切的合作。

[1] 臧正運博士目前於澳洲新南威爾斯大學法學院擔任Research Fellow，為「數位金融監理」研究團隊之成員。

[2] 白皮書將Regulatory Sandbox譯為「創新試驗場」。

＊作者為金融市場觀察家、金融科技新創投資人

加入Line好友
風傳媒歡迎各界分享發聲，來稿請寄至 service@stormmediagroup.com，並請附上姓名、聯絡方式、自我簡介，謝謝！
    """
    post(text)