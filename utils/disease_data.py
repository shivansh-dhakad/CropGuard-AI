# utils/disease_data.py
# Complete disease info mapping for all supported crops with English + Hindi support

DISEASE_INFO = {
    # ─── POTATO ───────────────────────────────────────────────────────────────
    "Potato___Early_blight": {
        "display_name": "Early Blight",
        "display_name_hi": "प्रारंभिक ब्लाइट",
        "symptoms": "Dark brown to black circular spots with concentric rings (target-board pattern) on lower/older leaves first. Yellowing around spots, premature leaf drop.",
        "symptoms_hi": "निचली और पुरानी पत्तियों पर पहले गहरे भूरे से काले रंग के गोल धब्बे जो केंद्र में लक्ष्य जैसी पट्टियाँ बनाते हैं। धब्बों के आसपास पीला पड़ना और समय से पहले पत्तियाँ झड़ना।",
        "causes": "Fungus Alternaria solani. Thrives in warm (24–29°C), humid conditions. Spreads via wind, rain splash, infected seed tubers.",
        "causes_hi": "फफूंद Alternaria solani। गर्म (24–29°C) और नम मौसम में तेजी से फैलता है। हवा, बारिश की छींटों और संक्रमित बीज आलू से फैलता है।",
        "recommendation": "Apply fungicides (chlorothalonil, mancozeb) at first sign. Remove infected leaves. Ensure proper spacing for airflow. Use certified disease-free seed potatoes. Rotate crops every 2–3 years.",
        "recommendation_hi": "पहले लक्षण दिखते ही फफूंदनाशक (क्लोरोथालोनिल, मैंकोजेब) स्प्रे करें। संक्रमित पत्तियाँ हटा दें। हवा के आवागमन के लिए पौधों के बीच उचित दूरी रखें। प्रमाणित रोग-मुक्त बीज आलू का उपयोग करें। फसल चक्रण हर 2-3 साल में करें।",
        "severity": "moderate"
    },
    "Potato___Late_blight": {
        "display_name": "Late Blight",
        "display_name_hi": "अंतिम ब्लाइट",
        "symptoms": "Water-soaked, pale green lesions on leaf edges turning dark brown/black with white mold underneath in humid conditions. Stems turn black. Tubers show copper-brown rot.",
        "symptoms_hi": "पत्तियों के किनारों पर पानी भरे हल्के हरे घाव जो नम मौसम में गहरे भूरे/काले हो जाते हैं और नीचे सफेद फफूंद दिखाई देती है। तने काले पड़ जाते हैं। कंदों में तांबे जैसा भूरा सड़न।",
        "causes": "Oomycete Phytophthora infestans. Favors cool (10–20°C), wet weather. Highly contagious — spreads within 2–3 days under ideal conditions.",
        "causes_hi": "ओओमाइसीट Phytophthora infestans। ठंडे (10–20°C) और गीले मौसम में तेजी से फैलता है। बहुत संक्रामक — आदर्श परिस्थितियों में 2-3 दिनों में पूरी फसल बर्बाद कर सकता है।",
        "recommendation": "Emergency: apply systemic fungicides (metalaxyl, cymoxanil) immediately. Destroy all infected plant material. Do NOT compost. Harvest tubers quickly if outbreak occurs. Plant resistant varieties (Sarpo Mira, etc.).",
        "recommendation_hi": "आपातकाल: तुरंत सिस्टेमिक फफूंदनाशक (मेटालैक्सिल, साइमॉक्सानिल) लगाएं। सभी संक्रमित पौध सामग्री नष्ट कर दें। कंपोस्ट न करें। यदि प्रकोप हो तो कंदों की तुरंत कटाई करें। प्रतिरोधी किस्में (सरपो मीरा आदि) लगाएं।",
        "severity": "severe"
    },
    "Potato___healthy": {
        "display_name": "Healthy",
        "display_name_hi": "स्वस्थ",
        "symptoms": "No visible symptoms. Leaves are vibrant green with no spots, lesions, or discoloration.",
        "symptoms_hi": "कोई दृश्य लक्षण नहीं। पत्तियाँ चमकदार हरी, बिना किसी धब्बे, घाव या रंग परिवर्तन के।",
        "causes": "Plant is in good health.",
        "causes_hi": "पौधा अच्छे स्वास्थ्य में है।",
        "recommendation": "Continue regular watering, balanced fertilization, and preventive fungicide schedule. Monitor weekly for early signs.",
        "recommendation_hi": "नियमित पानी दें, संतुलित खाद डालें और रोकथाम के लिए फफूंदनाशक का शेड्यूल बनाए रखें। हर सप्ताह प्रारंभिक लक्षणों की जाँच करें।",
        "severity": "none"
    },

    # ─── TOMATO ───────────────────────────────────────────────────────────────
    "Tomato___Bacterial_spot": {
        "display_name": "Bacterial Spot",
        "display_name_hi": "बैक्टीरियल स्पॉट",
        "symptoms": "Small, water-soaked spots on leaves becoming dark, raised scabs on fruit. Leaves may turn yellow and drop. Fruit quality severely impacted.",
        "symptoms_hi": "पत्तियों पर छोटे पानी भरे धब्बे जो बाद में गहरे और ऊपर उठे हुए घाव बन जाते हैं। फल पर भी प्रभाव पड़ता है। पत्तियाँ पीली पड़कर गिर सकती हैं।",
        "causes": "Bacteria Xanthomonas vesicatoria. Spread by rain splash, wind, contaminated tools, and infected seeds.",
        "causes_hi": "बैक्टीरिया Xanthomonas vesicatoria। बारिश की छींटों, हवा, दूषित औजारों और संक्रमित बीजों से फैलता है।",
        "recommendation": "Copper-based bactericides (copper hydroxide). Avoid overhead irrigation. Remove infected plant parts. Use disease-free transplants. Disinfect tools between plants.",
        "recommendation_hi": "कॉपर आधारित बैक्टीरियानाशक (कॉपर हाइड्रोक्साइड) का छिड़काव करें। ऊपर से पानी न दें। संक्रमित भाग हटा दें। रोग-मुक्त रोपे लगाएं। औजारों को बीच-बीच में कीटाणुरहित करें।",
        "severity": "moderate"
    },
    "Tomato___Early_blight": {
        "display_name": "Early Blight",
        "display_name_hi": "प्रारंभिक ब्लाइट",
        "symptoms": "Concentric ring spots (bull's-eye pattern) on older leaves. Yellow halo around spots. Stem lesions at soil line (collar rot). Fruit shows dark, sunken spots near stem.",
        "symptoms_hi": "पुरानी पत्तियों पर केंद्रित वलय वाले धब्बे (बुल्स आई पैटर्न)। धब्बों के चारों ओर पीला घेरा। तने पर मिट्टी की सतह के पास घाव (कॉलर रॉट)। फल पर तने के पास गहरे धँसे धब्बे।",
        "causes": "Fungus Alternaria solani. Common in warm (26–28°C), humid weather. Overwinters in soil and plant debris.",
        "causes_hi": "फफूंद Alternaria solani। गर्म (26–28°C) और नम मौसम में आम। मिट्टी और पौधे के अवशेषों में सर्दियों में जीवित रहता है।",
        "recommendation": "Apply chlorothalonil or copper fungicides preventively. Mulch to prevent soil splash. Remove lower leaves touching soil. Stake plants for better airflow. Practice 2-year crop rotation.",
        "recommendation_hi": "रोकथाम के लिए क्लोरोथालोनिल या कॉपर फफूंदनाशक लगाएं। मिट्टी के छींटे रोकने के लिए मल्चिंग करें। मिट्टी को छूने वाली निचली पत्तियाँ हटाएं। बेहतर हवा के लिए पौधों को सहारा दें। 2 वर्ष का फसल चक्रण अपनाएं।",
        "severity": "moderate"
    },
    "Tomato___Late_blight": {
        "display_name": "Late Blight",
        "display_name_hi": "अंतिम ब्लाइट",
        "symptoms": "Large, irregular water-soaked spots on leaves, rapidly turning brown/black. White fluffy growth on underside in humidity. Brown greasy spots on fruit.",
        "symptoms_hi": "पत्तियों पर बड़े अनियमित पानी भरे धब्बे जो तेजी से भूरे/काले हो जाते हैं। नमी में नीचे की सतह पर सफेद फूली हुई फफूंद। फल पर भूरे चिकने धब्बे।",
        "causes": "Phytophthora infestans. Cool nights (10–13°C) + warm humid days. Can destroy entire crop within a week.",
        "causes_hi": "Phytophthora infestans। ठंडी रातें (10–13°C) और गर्म नम दिन। एक सप्ताह में पूरी फसल नष्ट कर सकता है।",
        "recommendation": "Apply systemic fungicides (metalaxyl + mancozeb) at first sign. Increase plant spacing. Avoid evening irrigation. Destroy all infected material immediately.",
        "recommendation_hi": "पहले लक्षण पर सिस्टेमिक फफूंदनाशक (मेटालैक्सिल + मैंकोजेब) लगाएं। पौधों के बीच दूरी बढ़ाएं। शाम को पानी न दें। सभी संक्रमित सामग्री तुरंत नष्ट करें।",
        "severity": "severe"
    },
    "Tomato___Leaf_Mold": {
        "display_name": "Leaf Mold",
        "display_name_hi": "लीफ मोल्ड",
        "symptoms": "Yellow spots on upper leaf surface with olive-green to brown velvety mold patches on underside. Leaves curl upward, wilt, and drop in severe cases.",
        "symptoms_hi": "पत्ती की ऊपरी सतह पर पीले धब्बे और नीचे जैतून हरे से भूरे रंग का मखमली फफूंद। गंभीर मामलों में पत्तियाँ ऊपर की ओर मुड़ जाती हैं, मुरझा जाती हैं और गिर जाती हैं।",
        "causes": "Fungus Passalora fulva. Favors high humidity (>85%) and moderate temperatures (22–25°C). Common in greenhouse tomatoes.",
        "causes_hi": "फफूंद Passalora fulva। उच्च नमी (>85%) और मध्यम तापमान (22–25°C) में पनपता है। ग्रीनहाउस टमाटर में आम।",
        "recommendation": "Improve ventilation and reduce humidity. Apply fungicides (chlorothalonil, mancozeb). Remove infected leaves. Avoid wetting foliage when watering.",
        "recommendation_hi": "वेंटिलेशन बढ़ाएं और नमी कम करें। फफूंदनाशक (क्लोरोथालोनिल, मैंकोजेब) लगाएं। संक्रमित पत्तियाँ हटा दें। पानी देते समय पत्तियों को गीला न करें।",
        "severity": "moderate"
    },
    "Tomato___Septoria_leaf_spot": {
        "display_name": "Septoria Leaf Spot",
        "display_name_hi": "सेप्टोरिया लीफ स्पॉट",
        "symptoms": "Small circular spots (3–6mm) with dark brown borders and tan/grey centers. Tiny black dots (pycnidia) visible in spot centers. Starts on lower leaves, moves upward.",
        "symptoms_hi": "3-6 मिमी के छोटे गोल धब्बे जिनके किनारे गहरे भूरे और बीच हल्के भूरे/ग्रे होते हैं। धब्बे के केंद्र में छोटे काले बिंदु (पाइकनिडिया) दिखते हैं। निचली पत्तियों से शुरू होकर ऊपर की ओर बढ़ता है।",
        "causes": "Fungus Septoria lycopersici. Thrives in warm (20–25°C), wet conditions. Overwinters in soil and debris.",
        "causes_hi": "फफूंद Septoria lycopersici। गर्म (20–25°C) और गीले मौसम में पनपता है। मिट्टी और अवशेषों में सर्दी में जीवित रहता है।",
        "recommendation": "Remove and destroy infected leaves immediately. Apply protective fungicides (mancozeb, chlorothalonil). Stake plants for airflow. Mulch soil surface. Avoid working with wet plants.",
        "recommendation_hi": "संक्रमित पत्तियाँ तुरंत हटाकर नष्ट करें। सुरक्षा फफूंदनाशक (मैंकोजेब, क्लोरोथालोनिल) लगाएं। हवा के लिए पौधों को सहारा दें। मिट्टी पर मल्चिंग करें। गीले पौधों के साथ काम न करें।",
        "severity": "moderate"
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "display_name": "Spider Mites (Two-Spotted)",
        "display_name_hi": "स्पाइडर माइट्स (टू-स्पॉटेड)",
        "symptoms": "Fine stippling/bronzing on upper leaf surface. Fine webbing on underside of leaves. Leaves turn yellow, bronzed, then brown and drop. Severe: plant defoliation.",
        "symptoms_hi": "पत्ती की ऊपरी सतह पर बारीक बिंदु और कांस्य रंग। नीचे की सतह पर बारीक जाला। पत्तियाँ पीली, कांस्य फिर भूरी होकर गिर जाती हैं। गंभीर स्थिति में पौधे की सारी पत्तियाँ झड़ जाती हैं।",
        "causes": "Pest Tetranychus urticae. Thrives in hot (>27°C), dry, dusty conditions. Population can explode in 5–7 days.",
        "causes_hi": "कीट Tetranychus urticae। गर्म (>27°C), सूखे और धूल भरे मौसम में तेजी से बढ़ता है। 5-7 दिनों में संख्या बहुत बढ़ सकती है।",
        "recommendation": "Spray with water (high pressure) to dislodge mites. Apply miticides (abamectin, spiromesifen) or neem oil. Introduce predatory mites (Phytoseiulus persimilis). Maintain adequate irrigation to reduce plant stress.",
        "recommendation_hi": "उच्च दबाव वाले पानी से स्प्रे करके माइट्स को हटाएं। माइटिसाइड (एबामेक्टिन, स्पाइरोमेसिफेन) या नीम का तेल लगाएं। शिकारी माइट्स (Phytoseiulus persimilis) छोड़ें। पौधे पर तनाव कम करने के लिए पर्याप्त सिंचाई करें।",
        "severity": "moderate"
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "display_name": "Yellow Leaf Curl Virus",
        "display_name_hi": "येलो लीफ कर्ल वायरस",
        "symptoms": "Upward curling, yellowing of leaf margins. Stunted plant growth. Small, distorted leaves. Reduced fruit set, small hard fruits.",
        "symptoms_hi": "पत्तियों के किनारे ऊपर की ओर मुड़ना और पीला पड़ना। पौधे की वृद्धि रुकना। छोटी और विकृत पत्तियाँ। फल कम लगना और छोटे कड़े फल।",
        "causes": "TYLCV transmitted by whitefly (Bemisia tabaci). One of most destructive tomato viruses. No chemical cure once infected.",
        "causes_hi": "सफेद मक्खी (Bemisia tabaci) द्वारा फैलने वाला TYLCV वायरस। टमाटर का सबसे विनाशकारी वायरस। एक बार संक्रमित होने पर कोई रासायनिक इलाज नहीं।",
        "recommendation": "Control whitefly populations with insecticides (imidacloprid) or yellow sticky traps. Remove and destroy infected plants immediately. Plant resistant varieties. Use reflective mulches to repel whiteflies.",
        "recommendation_hi": "सफेद मक्खी को नियंत्रित करने के लिए इमिडाक्लोप्रिड या पीले चिपचिपे ट्रैप का उपयोग करें। संक्रमित पौधों को तुरंत हटाकर नष्ट करें। प्रतिरोधी किस्में लगाएं। सफेद मक्खी भगाने के लिए रिफ्लेक्टिव मल्च का उपयोग करें।",
        "severity": "severe"
    },
    "Tomato___Tomato_mosaic_virus": {
        "display_name": "Tomato Mosaic Virus",
        "display_name_hi": "टमाटर मोज़ेक वायरस",
        "symptoms": "Light/dark green mosaic mottling on leaves. Leaf distortion, fern-like appearance. Stunted growth. Fruit may show yellow blotches or internal browning.",
        "symptoms_hi": "पत्तियों पर हल्के और गहरे हरे रंग का मोज़ेक पैटर्न। पत्तियाँ विकृत और फ़र्न जैसी हो जाती हैं। वृद्धि रुकना। फल पर पीले धब्बे या अंदर से भूरापन।",
        "causes": "ToMV — highly stable virus, survives in soil/debris for 2 years. Spread by contact (hands, tools), infected seed.",
        "causes_hi": "ToMV — बहुत स्थिर वायरस, मिट्टी और अवशेषों में 2 साल तक जीवित रहता है। हाथ, औजार और संक्रमित बीज से फैलता है।",
        "recommendation": "No cure for infected plants — remove and destroy. Wash hands with soap before handling plants. Sterilize tools with bleach solution (10%). Use certified virus-free seeds. Plant resistant varieties (Tm-2a gene).",
        "recommendation_hi": "संक्रमित पौधों का कोई इलाज नहीं — उन्हें हटाकर नष्ट करें। पौधे को छूने से पहले हाथ साबुन से धोएं। औजारों को 10% ब्लीच घोल से कीटाणुरहित करें। प्रमाणित वायरस-मुक्त बीज उपयोग करें। प्रतिरोधी किस्में (Tm-2a जीन) लगाएं।",
        "severity": "severe"
    },
    "Tomato___healthy": {
        "display_name": "Healthy",
        "display_name_hi": "स्वस्थ",
        "symptoms": "No visible symptoms. Deep green, firm leaves with no spots, discoloration, or deformity.",
        "symptoms_hi": "कोई दृश्य लक्षण नहीं। गहरी हरी, मजबूत पत्तियाँ बिना किसी धब्बे, रंग परिवर्तन या विकृति के।",
        "causes": "Plant is in good health.",
        "causes_hi": "पौधा अच्छे स्वास्थ्य में है।",
        "recommendation": "Maintain regular watering schedule, proper nutrition (N-P-K balanced), and weekly monitoring. Apply preventive copper spray monthly.",
        "recommendation_hi": "नियमित पानी देने का शेड्यूल बनाए रखें, संतुलित पोषण (N-P-K) दें और हर सप्ताह निगरानी करें। हर महीने रोकथाम के लिए कॉपर स्प्रे करें।",
        "severity": "none"
    },

    # ─── STRAWBERRY ───────────────────────────────────────────────────────────
    "Strawberry___Leaf_Spot": {
        "display_name": "Leaf Spot",
        "display_name_hi": "लीफ स्पॉट",
        "symptoms": "Small purple to brown spots on leaves. Centers may dry and fall out, giving a shot-hole appearance.",
        "symptoms_hi": "पत्तियों पर छोटे बैंगनी से भूरे धब्बे। बीच का भाग सूखकर गिर सकता है जिससे शॉट-होल जैसा दिखाई देता है।",
        "causes": "Fungal infection (Mycosphaerella fragariae). Thrives in moist, humid conditions.",
        "causes_hi": "फफूंद संक्रमण (Mycosphaerella fragariae)। नम और आर्द्र मौसम में तेजी से फैलता है।",
        "recommendation": "Remove infected leaves. Apply fungicides like captan or copper. Improve airflow and avoid overhead watering.",
        "recommendation_hi": "संक्रमित पत्तियाँ हटा दें। कैप्टान या कॉपर फफूंदनाशक लगाएं। हवा का प्रवाह बढ़ाएं और ऊपर से पानी न दें।",
        "severity": "moderate"
    },
    "Strawberry___Powdery_Mildew_Leaf": {
        "display_name": "Powdery Mildew",
        "display_name_hi": "पाउडरी मिल्ड्यू",
        "symptoms": "White powdery coating on leaf surfaces. Leaves curl upward and turn reddish-purple.",
        "symptoms_hi": "पत्तियों की सतह पर सफेद पाउडर जैसा लेप। पत्तियाँ ऊपर की ओर मुड़ जाती हैं और लाल-बैंगनी हो जाती हैं।",
        "causes": "Fungus Podosphaera aphanis. Occurs in dry conditions with high humidity.",
        "causes_hi": "फफूंद Podosphaera aphanis। सूखे मौसम में उच्च नमी होने पर होता है।",
        "recommendation": "Apply sulfur or potassium bicarbonate sprays. Improve air circulation.",
        "recommendation_hi": "सल्फर या पोटैशियम बाइकार्बोनेट स्प्रे करें। हवा का संचार सुधारें।",
        "severity": "moderate"
    },
    "Strawberry___angular_leafspot": {
        "display_name": "Angular Leaf Spot",
        "display_name_hi": "एंगुलर लीफ स्पॉट",
        "symptoms": "Water-soaked angular lesions on leaves, turning dark brown or black. Lesions follow leaf veins.",
        "symptoms_hi": "पत्तियों पर पानी भरे कोणीय घाव जो गहरे भूरे या काले हो जाते हैं। घाव पत्ती की नसों के अनुसार फैलते हैं।",
        "causes": "Bacteria Xanthomonas fragariae. Spreads in cool, wet conditions.",
        "causes_hi": "बैक्टीरिया Xanthomonas fragariae। ठंडे और गीले मौसम में फैलता है।",
        "recommendation": "Avoid overhead irrigation. Use disease-free plants. Apply copper sprays.",
        "recommendation_hi": "ऊपर से पानी देने से बचें। रोग-मुक्त पौधे लगाएं। कॉपर स्प्रे करें।",
        "severity": "moderate"
    },
    "Strawberry___healthy": {
        "display_name": "Healthy",
        "display_name_hi": "स्वस्थ",
        "symptoms": "No symptoms. Bright green, glossy leaves with no spots or discoloration.",
        "symptoms_hi": "कोई लक्षण नहीं। चमकदार हरी, चमकदार पत्तियाँ बिना किसी धब्बे या रंग परिवर्तन के।",
        "causes": "Plant is in good health.",
        "causes_hi": "पौधा अच्छे स्वास्थ्य में है।",
        "recommendation": "Continue mulching to prevent soil splash, balanced fertilization, and regular monitoring for pests/disease.",
        "recommendation_hi": "मिट्टी के छींटे रोकने के लिए मल्चिंग जारी रखें, संतुलित खाद डालें और कीट/रोग की नियमित निगरानी करें।",
        "severity": "none"
    },

    # ─── GRAPE ────────────────────────────────────────────────────────────────
    "Grape___Black_rot": {
        "display_name": "Black Rot",
        "display_name_hi": "ब्लैक रॉट",
        "symptoms": "Tan/brown circular spots with dark borders on leaves. Infected berries turn brown, then shrivel into hard black mummies hanging on cluster.",
        "symptoms_hi": "पत्तियों पर हल्के भूरे गोल धब्बे जिनके किनारे गहरे होते हैं। संक्रमित अंगूर भूरे होकर सिकुड़ जाते हैं और काली सख्त ममी बनकर गुच्छे पर लटक जाते हैं।",
        "causes": "Fungus Guignardia bidwellii. Thrives in warm (26°C), humid conditions. Overwinters in mummified fruit and canes.",
        "causes_hi": "फफूंद Guignardia bidwellii। गर्म (26°C) और नम मौसम में पनपता है। सर्दियों में ममी बने फल और डंठलों में जीवित रहता है।",
        "recommendation": "Apply fungicides (myclobutanil, mancozeb) from bud break. Remove all mummified fruit and infected canes. Ensure canopy airflow through proper pruning. Destroy infected debris.",
        "recommendation_hi": "कलियों के फूटने से ही फफूंदनाशक (माइक्लोबुटानिल, मैंकोजेब) लगाएं। सभी ममी बने फल और संक्रमित डंठल हटा दें। सही छंटाई से हवा का प्रवाह सुनिश्चित करें। संक्रमित अवशेष नष्ट करें।",
        "severity": "severe"
    },
    "Grape___Esca_(Black_Measles)": {
        "display_name": "Esca (Black Measles)",
        "display_name_hi": "एस्का (ब्लैक मीजल्स)",
        "symptoms": "Tiger-stripe pattern (yellow/red between veins) on leaves. Berries show dark spots ('measles'). Shoots may wilt suddenly. Internal wood shows dark streaking.",
        "symptoms_hi": "पत्तियों पर टाइगर स्ट्राइप पैटर्न (नसों के बीच पीला/लाल)। अंगूर पर काले धब्बे ('मीजल्स')। शाखाएँ अचानक मुरझा सकती हैं। अंदरूनी लकड़ी में काली धारियाँ।",
        "causes": "Complex of wood-rotting fungi (Phaeomoniella, Phaeoacremonium). Enters through pruning wounds. Chronic, progressive disease.",
        "causes_hi": "लकड़ी सड़ाने वाली फफूंदों का कॉम्प्लेक्स। छंटाई के घावों से प्रवेश करता है। पुरानी और बढ़ती हुई बीमारी।",
        "recommendation": "No cure for infected vines. Apply wound sealants (Bordeaux paste) immediately after pruning. Remove severely infected vines. Avoid pruning in wet weather. Research biological controls (Trichoderma).",
        "recommendation_hi": "संक्रमित बेलों का कोई इलाज नहीं। छंटाई के तुरंत बाद घाव पर बोर्डो पेस्ट लगाएं। गंभीर संक्रमित बेलें हटा दें। गीले मौसम में छंटाई न करें। जैविक नियंत्रण (ट्राइकोडर्मा) पर शोध करें।",
        "severity": "severe"
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "display_name": "Leaf Blight (Isariopsis)",
        "display_name_hi": "लीफ ब्लाइट (इसारियोप्सिस)",
        "symptoms": "Dark brown, irregular spots on leaves with yellow margins. Spots may coalesce. Premature defoliation weakening the vine.",
        "symptoms_hi": "पत्तियों पर गहरे भूरे अनियमित धब्बे जिनके किनारे पीले होते हैं। धब्बे आपस में मिल सकते हैं। समय से पहले पत्तियाँ झड़ने से बेल कमजोर हो जाती है।",
        "causes": "Fungus Isariopsis clavispora. Associated with warm, humid conditions. Usually secondary to other stresses.",
        "causes_hi": "फफूंद Isariopsis clavispora। गर्म और नम मौसम से जुड़ी। आमतौर पर अन्य तनावों के कारण होती है।",
        "recommendation": "Apply copper-based fungicides. Improve canopy management. Remove infected leaves. Ensure adequate nutrition to reduce stress.",
        "recommendation_hi": "कॉपर आधारित फफूंदनाशक लगाएं। कैनोपी प्रबंधन सुधारें। संक्रमित पत्तियाँ हटा दें। तनाव कम करने के लिए पर्याप्त पोषण दें।",
        "severity": "moderate"
    },
    "Grape___healthy": {
        "display_name": "Healthy",
        "display_name_hi": "स्वस्थ",
        "symptoms": "No symptoms. Vibrant green leaves, no spots or discoloration.",
        "symptoms_hi": "कोई लक्षण नहीं। चमकदार हरी पत्तियाँ, बिना किसी धब्बे या रंग परिवर्तन के।",
        "causes": "Plant is in good health.",
        "causes_hi": "पौधा अच्छे स्वास्थ्य में है।",
        "recommendation": "Maintain regular pruning for airflow, balanced fertilization, and weekly scouting for pests and disease signs.",
        "recommendation_hi": "हवा के लिए नियमित छंटाई, संतुलित खाद और कीट/रोग के लिए साप्ताहिक निगरानी बनाए रखें।",
        "severity": "none"
    },

    # ─── BANANA ───────────────────────────────────────────────────────────────
    "Banana___cordana": {
        "display_name": "Cordana Leaf Spot",
        "display_name_hi": "कोर्डाना लीफ स्पॉट",
        "symptoms": "Oval to elongated pale brown spots with yellow halos, mainly on older leaves. Spots may have darker brown borders. Reduces photosynthesis.",
        "symptoms_hi": "अंडाकार से लंबे हल्के भूरे धब्बे जिनके चारों ओर पीला घेरा होता है, मुख्यतः पुरानी पत्तियों पर। धब्बों के किनारे गहरे भूरे हो सकते हैं। प्रकाश संश्लेषण कम होता है।",
        "causes": "Fungus Cordana musae. Favors high humidity and poor drainage. Usually secondary opportunistic infection.",
        "causes_hi": "फफूंद Cordana musae। उच्च नमी और खराब जल निकासी में बढ़ता है। आमतौर पर द्वितीयक संक्रमण।",
        "recommendation": "Apply systemic fungicides (propiconazole, tebuconazole). Remove infected leaves. Improve drainage. Ensure adequate potassium nutrition for plant resistance.",
        "recommendation_hi": "सिस्टेमिक फफूंदनाशक (प्रोपिकोनाजोल, टेबुकोनाजोल) लगाएं। संक्रमित पत्तियाँ हटा दें। जल निकासी सुधारें। पौधे की प्रतिरोधक क्षमता बढ़ाने के लिए पर्याप्त पोटैशियम दें।",
        "severity": "mild"
    },
    "Banana___pestalotiopsis": {
        "display_name": "Pestalotiopsis Leaf Spot",
        "display_name_hi": "पेस्टालोटियोप्सिस लीफ स्पॉट",
        "symptoms": "Grey-brown spots with dark borders and yellow halos. Small black fruiting bodies visible in lesion centers. Multiple spots merge causing large dead areas.",
        "symptoms_hi": "ग्रे-भूरे धब्बे जिनके किनारे गहरे और पीला घेरा होता है। घाव के केंद्र में छोटे काले फलन शरीर दिखते हैं। कई धब्बे मिलकर बड़े मृत क्षेत्र बना देते हैं।",
        "causes": "Fungus Pestalotiopsis spp. Associated with plant stress (drought, wounds, nutrient deficiency). Opportunistic pathogen.",
        "causes_hi": "फफूंद Pestalotiopsis spp. पौधे के तनाव (सूखा, घाव, पोषक तत्वों की कमी) से जुड़ी। अवसरवादी रोगाणु।",
        "recommendation": "Reduce plant stress (adequate irrigation and nutrition). Apply fungicides (mancozeb, copper). Remove heavily infected leaves. Improve overall plant vigor.",
        "recommendation_hi": "पौधे का तनाव कम करें (पर्याप्त सिंचाई और पोषण)। फफूंदनाशक (मैंकोजेब, कॉपर) लगाएं। भारी संक्रमित पत्तियाँ हटा दें। पौधे की समग्र ताकत बढ़ाएं।",
        "severity": "mild"
    },
    "Banana___sigatoka": {
        "display_name": "Sigatoka Leaf Spot",
        "display_name_hi": "सिगाटोका लीफ स्पॉट",
        "symptoms": "Yellow streaks on leaves becoming brown oval spots with grey centers and yellow margins. Severe cases: entire leaves turn yellow and die prematurely.",
        "symptoms_hi": "पत्तियों पर पीली धारियाँ जो बाद में भूरे अंडाकार धब्बों में बदल जाती हैं जिनके केंद्र ग्रे और किनारे पीले होते हैं। गंभीर मामलों में पूरी पत्ती पीली पड़कर समय से पहले मर जाती है।",
        "causes": "Fungus Mycosphaerella musicola. Thrives in warm (25–28°C), humid, rainy conditions. Major yield-reducing disease worldwide.",
        "causes_hi": "फफूंद Mycosphaerella musicola। गर्म (25–28°C), नम और बारिश वाले मौसम में पनपता है। विश्व स्तर पर उपज कम करने वाली प्रमुख बीमारी।",
        "recommendation": "Apply fungicides (propiconazole, trifloxystrobin) on regular schedule. Remove infected leaves ('deleafing'). Ensure good drainage and airflow. Use resistant Cavendish sub-varieties where available.",
        "recommendation_hi": "नियमित अंतराल पर फफूंदनाशक (प्रोपिकोनाजोल, ट्राइफ्लॉक्सिस्ट्रोबिन) लगाएं। संक्रमित पत्तियाँ हटाएं ('डिलीफिंग')। अच्छी जल निकासी और हवा का प्रवाह सुनिश्चित करें। उपलब्ध होने पर प्रतिरोधी कैवेंडिश किस्में लगाएं।",
        "severity": "moderate"
    },
    "Banana___healthy": {
        "display_name": "Healthy",
        "display_name_hi": "स्वस्थ",
        "symptoms": "No symptoms. Deep green, intact leaves with no spots or yellowing.",
        "symptoms_hi": "कोई लक्षण नहीं। गहरी हरी, पूरी पत्तियाँ बिना किसी धब्बे या पीलेपन के।",
        "causes": "Plant is in good health.",
        "causes_hi": "पौधा अच्छे स्वास्थ्य में है।",
        "recommendation": "Maintain regular fertilization schedule (especially potassium), irrigation management, and monthly disease scouting.",
        "recommendation_hi": "नियमित खाद (खासकर पोटैशियम) का शेड्यूल, सिंचाई प्रबंधन और हर महीने रोग जाँच बनाए रखें।",
        "severity": "none"
    },

    # ─── MANGO ────────────────────────────────────────────────────────────────
    "Mango___Anthracnose": {
        "display_name": "Anthracnose",
        "display_name_hi": "एंथ्रेक्नोज",
        "symptoms": "Dark, sunken, irregular spots on leaves, twigs, and fruit. Black lesions on flowers causing blossom blight. Fruit shows black sunken rot, particularly post-harvest.",
        "symptoms_hi": "पत्तियों, टहनियों और फलों पर गहरे, धँसे हुए अनियमित धब्बे। फूलों पर काले घाव जिससे फूल झड़ जाते हैं। फल पर काला धँसा सड़न, खासकर कटाई के बाद।",
        "causes": "Fungus Colletotrichum gloeosporioides. Thrives in warm (25–30°C), humid, rainy weather during flowering. Latent infection in fruit.",
        "causes_hi": "फफूंद Colletotrichum gloeosporioides। फूल आने के समय गर्म (25–30°C), नम और बारिश वाले मौसम में तेजी से फैलता है। फल में छिपा संक्रमण रह सकता है।",
        "recommendation": "Apply fungicides (mancozeb, copper hydroxide, carbendazim) before and during flowering. Hot water treatment of harvested fruit (52°C for 5 min). Post-harvest fungicide dips. Plant in well-drained areas with good airflow.",
        "recommendation_hi": "फूल आने से पहले और दौरान फफूंदनाशक (मैंकोजेब, कॉपर हाइड्रोक्साइड, कार्बेन्डाजिम) लगाएं। कटे फलों का गर्म पानी उपचार (52°C पर 5 मिनट)। कटाई के बाद फफूंदनाशक डुबोकर उपचार। अच्छी जल निकासी और हवा वाले स्थान पर लगाएं।",
        "severity": "severe"
    },
    "Mango___Powdery_Mildew": {
        "display_name": "Powdery Mildew",
        "display_name_hi": "पाउडरी मिल्ड्यू",
        "symptoms": "White powdery coating on young leaves, panicles, and fruit. Infected flowers and small fruit drop. Affected leaves may curl and distort.",
        "symptoms_hi": "नई पत्तियों, पुष्प गुच्छों और फलों पर सफेद पाउडर जैसा लेप। संक्रमित फूल और छोटे फल झड़ जाते हैं। प्रभावित पत्तियाँ मुड़ और विकृत हो सकती हैं।",
        "causes": "Fungus Oidium mangiferae. Favors dry weather with cool nights and warm days (10–30°C range). Critical during flowering season.",
        "causes_hi": "फफूंद Oidium mangiferae। सूखे मौसम में ठंडी रातें और गर्म दिन (10–30°C) में पनपता है। फूल आने के मौसम में बहुत महत्वपूर्ण।",
        "recommendation": "Apply sulfur-based fungicides or wettable sulfur at 10-day intervals during flowering. Karathane (dinocap) is highly effective. Spray in early morning. Avoid evening sprays. Prune for open canopy.",
        "recommendation_hi": "फूल आने के दौरान 10 दिन के अंतराल पर सल्फर आधारित फफूंदनाशक या वेटेबल सल्फर लगाएं। कराथेन (डाइनोकैप) बहुत प्रभावी है। सुबह जल्दी स्प्रे करें। शाम को स्प्रे न करें। खुली छत्रछाया के लिए छंटाई करें।",
        "severity": "moderate"
    },
    "Mango___Sooty_Mould": {
        "display_name": "Sooty Mould",
        "display_name_hi": "सूटी मोल्ड",
        "symptoms": "Black sooty coating on leaf surfaces. Reduces photosynthesis. Usually indicates insect infestation (mealybugs, scale insects) as the mould grows on insect honeydew.",
        "symptoms_hi": "पत्तियों की सतह पर काला सूटी जैसा लेप। प्रकाश संश्लेषण कम होता है। आमतौर पर कीट संक्रमण (मिलीबग, स्केल इंसेक्ट) का संकेत है क्योंकि फफूंद कीटों के मधुरस पर उगती है।",
        "causes": "Saprophytic fungi (Capnodium, Meliola) growing on honeydew secretions of sap-sucking insects. Not directly pathogenic but symptom of pest problem.",
        "causes_hi": "सैप्रोफाइटिक फफूंद (Capnodium, Meliola) जो रस चूसने वाले कीटों के मधुरस पर बढ़ती है। सीधे रोगकारी नहीं लेकिन कीट समस्या का लक्षण।",
        "recommendation": "FIRST: control the insect causing honeydew (spray imidacloprid or neem oil for mealybugs/scale). Wash mould off with water spray. Starch spray (2%) can help remove mould coating. Improve canopy airflow.",
        "recommendation_hi": "सबसे पहले मधुरस पैदा करने वाले कीट को नियंत्रित करें (मिलीबग/स्केल के लिए इमिडाक्लोप्रिड या नीम तेल स्प्रे करें)। पानी के छिड़काव से फफूंद हटाएं। 2% स्टार्च स्प्रे फफूंद हटाने में मदद कर सकता है। हवा का प्रवाह बढ़ाएं।",
        "severity": "mild"
    },
    "Mango___healthy": {
        "display_name": "Healthy",
        "display_name_hi": "स्वस्थ",
        "symptoms": "No symptoms. Dark green, glossy leaves with no spots or discoloration.",
        "symptoms_hi": "कोई लक्षण नहीं। गहरी हरी, चमकदार पत्तियाँ बिना किसी धब्बे या रंग परिवर्तन के।",
        "causes": "Plant is in good health.",
        "causes_hi": "पौधा अच्छे स्वास्थ्य में है।",
        "recommendation": "Apply preventive copper fungicide spray before flowering season. Maintain regular irrigation and fertilization schedule.",
        "recommendation_hi": "फूल आने के मौसम से पहले रोकथाम के लिए कॉपर फफूंदनाशक स्प्रे करें। नियमित सिंचाई और खाद का शेड्यूल बनाए रखें।",
        "severity": "none"
    },
    "Mango___Bacterial_Canker": {
        "display_name": "Bacterial Canker",
        "display_name_hi": "बैक्टीरियल कैंकर",
        "symptoms": "Dark angular leaf spots with yellow halo. Cracks in bark, gum oozing from stem. Fruit may develop black lesions.",
        "symptoms_hi": "पत्तियों पर गहरे कोणीय धब्बे जिनके चारों ओर पीला घेरा। छाल में दरारें, तने से गोंद रिसना। फल पर काले घाव बन सकते हैं।",
        "causes": "Bacteria Xanthomonas campestris. Spread through rain splash and infected tools.",
        "causes_hi": "बैक्टीरिया Xanthomonas campestris। बारिश की छींटों और संक्रमित औजारों से फैलता है।",
        "recommendation": "Prune infected branches. Apply copper-based bactericides. Avoid overhead irrigation. Disinfect tools.",
        "recommendation_hi": "संक्रमित शाखाएँ काट दें। कॉपर आधारित बैक्टीरियानाशक लगाएं। ऊपर से पानी न दें। औजारों को कीटाणुरहित करें।",
        "severity": "moderate"
    },
    "Mango___Gall_Midge": {
        "display_name": "Gall Midge",
        "display_name_hi": "गॉल मिज",
        "symptoms": "Small blister-like galls on leaves. Leaves curl and become deformed. Severe infestation reduces growth.",
        "symptoms_hi": "पत्तियों पर छोटे फफोले जैसे गॉल। पत्तियाँ मुड़ जाती हैं और विकृत हो जाती हैं। गंभीर संक्रमण से वृद्धि रुक जाती है।",
        "causes": "Insect pest Procontarinia matteiana. Larvae feed inside leaf tissues.",
        "causes_hi": "कीट Procontarinia matteiana। लार्वा पत्ती के अंदर भोजन करते हैं।",
        "recommendation": "Spray insecticides (imidacloprid or neem oil). Remove and destroy infected leaves.",
        "recommendation_hi": "कीटनाशक (इमिडाक्लोप्रिड या नीम तेल) का छिड़काव करें। संक्रमित पत्तियाँ हटाकर नष्ट करें।",
        "severity": "moderate"
    },
}

# ── TRANSLATIONS ──────────────────────────────────────────────────────────────
# (Your existing TRANSLATIONS dictionary remains unchanged)
TRANSLATIONS = {
    "en": {
        "app_title": "CropGuard AI",
        "app_subtitle": "Plant Disease Detection System",
        "upload_title": "Analyze Your Crop",
        "upload_desc": "Upload a clear photo of the affected plant leaf for instant AI diagnosis",
        "upload_btn": "Upload Image",
        "camera_btn": "Use Camera",
        "capture_btn": "Capture",
        "retake_btn": "Retake",
        "analyze_btn": "Analyze Plant",
        "back_btn": "← New Analysis",
        "crop_label": "Detected Crop",
        "disease_label": "Diagnosis",
        "symptoms_label": "Symptoms",
        "causes_label": "Causes",
        "recommendation_label": "Recommendation",
        "severity_label": "Severity Level",
        "unsupported_title": "Crop Not Supported",
        "unsupported_msg": "This crop is not in our database yet. Supported crops: Potato, Tomato, Strawberry, Grape, Banana, Mango.",
        "disclaimer": "⚠️ This tool is for educational purposes only and is not professional agricultural advice. Consult a certified agronomist for critical decisions.",
        "analyzing": "Analyzing...",
        "severity_none": "None — Healthy",
        "severity_mild": "Mild",
        "severity_moderate": "Moderate",
        "severity_severe": "Severe",
        "drag_drop": "or drag & drop image here",
        "loading_text": "Initializing AI models...",
        "healthy_badge": "✓ Healthy Plant",
        "confidence": "Confidence",
    },
    "hi": {
        "app_title": "CropGuard AI",
        "app_subtitle": "पौधा रोग पहचान प्रणाली",
        "upload_title": "अपनी फसल की जाँच करें",
        "upload_desc": "तत्काल AI निदान के लिए प्रभावित पत्ती की स्पष्ट फोटो अपलोड करें",
        "upload_btn": "छवि अपलोड करें",
        "camera_btn": "कैमरा खोलें",
        "capture_btn": "तस्वीर लें",
        "retake_btn": "फिर से लें",
        "analyze_btn": "पौधे की जाँच करें",
        "back_btn": "← नई जाँच",
        "crop_label": "पहचानी गई फसल",
        "disease_label": "रोग निदान",
        "symptoms_label": "लक्षण",
        "causes_label": "कारण",
        "recommendation_label": "उपचार सुझाव",
        "severity_label": "गंभीरता स्तर",
        "unsupported_title": "फसल समर्थित नहीं",
        "unsupported_msg": "यह फसल अभी हमारे डेटाबेस में नहीं है। समर्थित फसलें: आलू, टमाटर, स्ट्रॉबेरी, अंगूर, केला, आम।",
        "disclaimer": "⚠️ यह उपकरण केवल शैक्षिक उद्देश्यों के लिए है और पेशेवर कृषि सलाह नहीं है। महत्वपूर्ण निर्णयों के लिए प्रमाणित कृषि विशेषज्ञ से परामर्श लें।",
        "analyzing": "विश्लेषण हो रहा है...",
        "severity_none": "कोई नहीं — स्वस्थ",
        "severity_mild": "हल्का",
        "severity_moderate": "मध्यम",
        "severity_severe": "गंभीर",
        "drag_drop": "या यहाँ छवि खींचें और छोड़ें",
        "loading_text": "AI मॉडल प्रारंभ हो रहे हैं...",
        "healthy_badge": "✓ स्वस्थ पौधा",
        "confidence": "विश्वास",
    }
}