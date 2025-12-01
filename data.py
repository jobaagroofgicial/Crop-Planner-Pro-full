# data.py — Crop database for Crop Planner Pro
# All names in Bangla where appropriate

crop_data = {
    "টমেটো": {
        "seed_rate": "৩০–৪০ গ্রাম/বিঘা",
        "expected_yield": "৮০০–১২০০ কেজি/বিঘা",
        "yield_per_bigha": 1000,
        "fertilizer": {
            "Base (at planting)": {"Urea (kg)": 25, "TSP (kg)": 20, "MOP (kg)": 15},
            "Topdress 15 days": {"Urea (kg)": 8, "MOP (kg)": 3},
            "Topdress 30 days": {"Urea (kg)": 10, "MOP (kg)": 4},
            "Topdress 50 days": {"Urea (kg)": 5, "MOP (kg)": 5}
        },
        "spray_schedule": [
            {"day": 7, "task": "Seedling check — damping off prevention", "spray": "Ridomil Gold 2 g/L (preventive)"},
            {"day": 14, "task": "Early leaf spray", "spray": "Amistar Top 1.5 mL/L"},
            {"day": 21, "task": "Fungal protection", "spray": "Mancozeb 2 g/L"},
            {"day": 28, "task": "Preventive fungicide", "spray": "Contact fungicide (as label)"},
            {"day": 35, "task": "Fruit borer control", "spray": "Spinosad (as label)"},
            {"day": 42, "task": "Whitefly/aphid check", "spray": "Imidacloprid (soil/foliar per label)"},
            {"day": 49, "task": "Late blight monitor", "spray": "Copper fungicide per label"},
            {"day": 56, "task": "Fruit rot prevention", "spray": "Ridomil 2 g/L"},
            {"day": 63, "task": "Final pre-harvest spray", "spray": "Avoid residues — use safe option"},
            {"day": 70, "task": "Post-harvest field sanitation", "spray": "Field sanitation — remove debris"}
        ],
        "pest_notes": [
            "Early blight and late blight are common; rotate fields and remove debris.",
            "Fruit borer management with pheromone traps and timely sprays."
        ],
        "rotation": [
            {"year": 1, "crop": "টমেটো"},
            {"year": 2, "crop": "ভুট্টা / মাইড সিজন ধান"},
            {"year": 3, "crop": "করলা / শসা"},
            {"year": 4, "crop": "ডাল জাতীয় ফসল / তরমুজ"}
        ],
        "cost": 35000,
        "sell_rate": 30
    },

    "করলা": {
        "seed_rate": "১.৫–২ কেজি/বিঘা",
        "expected_yield": "১২০০–১৫০০ কেজি/বিঘা",
        "yield_per_bigha": 1300,
        "fertilizer": {
            "Base (at planting)": {"Urea (kg)": 15, "TSP (kg)": 12, "MOP (kg)": 10},
            "Topdress 20 days": {"Urea (kg)": 6, "MOP (kg)": 3},
            "Topdress 35 days": {"Urea (kg)": 6, "MOP (kg)": 4}
        },
        "spray_schedule": [
            {"day": 10, "task": "Downy mildew prevention", "spray": "Rovral 2 g/L"},
            {"day": 17, "task": "Fruit fly monitoring", "spray": "Methyl eugenol traps + Deltamethrin as needed"},
            {"day": 24, "task": "Mite control", "spray": "Omite or approved acaricide"},
            {"day": 31, "task": "Fungal check", "spray": "Ridomil 2 g/L"},
            {"day": 38, "task": "Fruit fly control", "spray": "Trapping + field sanitation"},
            {"day": 45, "task": "Leaf spot control", "spray": "Mancozeb 2 g/L"},
            {"day": 52, "task": "Mite control follow-up", "spray": "Omite"},
            {"day": 59, "task": "Preventive fungicide", "spray": "Antracol or similar"},
            {"day": 66, "task": "Insect check", "spray": "Cypermethrin if severe"},
            {"day": 73, "task": "Pre-harvest sanitation", "spray": "Field sanitation"}
        ],
        "pest_notes": [
            "Fruit fly causes major losses; use traps and field sanitation.",
            "Rotate crops to reduce soil-borne pathogens."
        ],
        "rotation": [
            {"year": 1, "crop": "করলা"},
            {"year": 2, "crop": "শসা / ভুট্টা"},
            {"year": 3, "crop": "ডাল জাতীয় ফসল"},
            {"year": 4, "crop": "তরমুজ / ধান"}
        ],
        "cost": 28000,
        "sell_rate": 35
    },

    "শসা": {
        "seed_rate": "০.৮–১ কেজি/বিঘা",
        "expected_yield": "১০০০–১৩০০ কেজি/বিঘা",
        "yield_per_bigha": 1100,
        "fertilizer": {
            "Base (planting)": {"Urea (kg)": 18, "TSP (kg)": 12, "MOP (kg)": 12},
            "Topdress 15 days": {"Urea (kg)": 7, "MOP (kg)": 3},
            "Topdress 30 days": {"Urea (kg)": 7, "MOP (kg)": 4}
        },
        "spray_schedule": [
            {"day": 7, "task": "Powdery mildew prevention", "spray": "Sulfur per label"},
            {"day": 14, "task": "Fruit fly control", "spray": "Deltamethrin / traps"},
            {"day": 21, "task": "Leaf spot control", "spray": "Mancozeb"},
            {"day": 28, "task": "Powdery mildew follow-up", "spray": "Sulfur"},
            {"day": 35, "task": "Mite control", "spray": "Omite"},
            {"day": 42, "task": "Downy mildew check", "spray": "Ridomil"},
            {"day": 49, "task": "Fruit fly follow-up", "spray": "Trapping + insecticide"},
            {"day": 56, "task": "Leaf spot follow-up", "spray": "Antracol"},
            {"day": 63, "task": "Mite follow-up", "spray": "Omite"},
            {"day": 70, "task": "Pre-harvest check", "spray": "Avoid harmful residues"}
        ],
        "pest_notes": [
            "Fruit fly, powdery mildew and mites are common. Use traps and sulfur for prevention."
        ],
        "rotation": [
            {"year": 1, "crop": "শসা"},
            {"year": 2, "crop": "ধান / ভুট্টা"},
            {"year": 3, "crop": "ডাল জাতীয়"},
            {"year": 4, "crop": "শাক/মূল/বাঁধাকপি"}
        ],
        "cost": 25000,
        "sell_rate": 25
    },

    "বেগুন": {
        "seed_rate": "১–১.৫ কেজি/বিঘা",
        "expected_yield": "৯০০–১১০০ কেজি/বিঘা",
        "yield_per_bigha": 1000,
        "fertilizer": {"Base": {"Urea (kg)":20, "TSP (kg)":15, "MOP (kg)":12}, "Topdress": {"Urea (kg)":10}},
        "spray_schedule": [
            {"day":7,"task":"Seedling check","spray":"Preventive fungicide"},
            {"day":14,"task":"Aphid/whitefly check","spray":"Imidacloprid per label"},
            {"day":21,"task":"Fruit borer control","spray":"Emamectin benzoate / Spinosad"},
            {"day":28,"task":"Fungal control","spray":"Mancozeb"},
            {"day":35,"task":"Mite / thrips check","spray":"Acaricide"},
            {"day":42,"task":"Fruit borer follow-up","spray":"As label"},
            {"day":49,"task":"Pre-harvest hygiene","spray":"Field sanitation"},
            {"day":56,"task":"Soil health check","spray":"—"},
            {"day":63,"task":"Final pre-harvest","spray":"Safe option"},
            {"day":70,"task":"Post-harvest care","spray":"Remove debris"}
        ],
        "pest_notes":["Fruit borer and whitefly common; use pheromone trapping and timely sprays."],
        "rotation":[{"year":1,"crop":"বেগুন"},{"year":2,"crop":"ভুট্টা / ধান"},{"year":3,"crop":"ডাল জাতীয়"},{"year":4,"crop":"শাক জাতীয়"}],
        "cost":30000,
        "sell_rate":28
    },

    "মরিচ (লং/চিলি)": {
        "seed_rate":"০.৫–১ কেজি/বিঘা",
        "expected_yield":"৬০০–৯০০ কেজি/বিঘা",
        "yield_per_bigha":750,
        "fertilizer":{"Base":{"Urea (kg)":18,"TSP (kg)":12,"MOP (kg)":10}},
        "spray_schedule":[
            {"day":7,"task":"Seedling health","spray":"Fungicide as preventive"},
            {"day":14,"task":"Aphid / thrips check","spray":"Imidacloprid"},
            {"day":21,"task":"Bacterial spot monitor","spray":"Copper spray"},
            {"day":28,"task":"Fruit borer / worm check","spray":"Spinosad"},
            {"day":35,"task":"General fungal control","spray":"Mancozeb"},
            {"day":42,"task":"Mite control","spray":"Acaricide"},
            {"day":49,"task":"Pre-harvest check","spray":"Avoid residues"},
            {"day":56,"task":"Post-harvest sanitation","spray":"Field sanitation"},
            {"day":63,"task":"Pheromone trap check","spray":"—"},
            {"day":70,"task":"Final check","spray":"—"}
        ],
        "pest_notes":["Aphids, thrips and fruit borers common."],
        "rotation":[{"year":1,"crop":"মরিচ"},{"year":2,"crop":"শসা / করলা"},{"year":3,"crop":"ডাল জাতীয়"},{"year":4,"crop":"ভুট্টা"}],
        "cost":22000,
        "sell_rate":60
    },

    "কুমড়া / কুমড়া (Pumpkin)": {
        "seed_rate":"১–১.৫ কেজি/বিঘা",
        "expected_yield":"৮০০–১২০০ কেজি/বিঘা",
        "yield_per_bigha":900,
        "fertilizer":{"Base":{"Urea (kg)":20,"TSP (kg)":15,"MOP (kg)":12}},
        "spray_schedule":[
            {"day":10,"task":"Powdery mildew prevention","spray":"Sulfur"},
            {"day":20,"task":"Fruit fly trap setup","spray":"Traps + insecticide"},
            {"day":30,"task":"General fungal control","spray":"Mancozeb"},
            {"day":40,"task":"Aphid check","spray":"Imidacloprid"},
            {"day":50,"task":"Mite control","spray":"Acaricide"},
            {"day":60,"task":"Pre-harvest check","spray":"—"},
            {"day":70,"task":"Harvest prep","spray":"—"},
            {"day":80,"task":"Post-harvest sanitation","spray":"—"},
            {"day":90,"task":"Soil care","spray":"—"},
            {"day":100,"task":"Field cleanup","spray":"—"}
        ],
        "pest_notes":["Fruit fly and powdery mildew are important issues."],
        "rotation":[{"year":1,"crop":"কুমড়া"},{"year":2,"crop":"শসা / ভুট্টা"},{"year":3,"crop":"ডাল"},{"year":4,"crop":"শাক"}],
        "cost":20000,
        "sell_rate":18
    },

    "রোষ্টকার্ট (Beetroot)": {
        "seed_rate":"০.৫ কেজি/বিঘা",
        "expected_yield":"৬০০–৮০০ কেজি/বিঘা",
        "yield_per_bigha":700,
        "fertilizer":{"Base":{"Urea (kg)":12,"TSP (kg)":15,"MOP (kg)":10}},
        "spray_schedule":[
            {"day":7,"task":"Seedling check","spray":"—"},
            {"day":14,"task":"Leaf miner check","spray":"Insecticide if needed"},
            {"day":21,"task":"Fungal monitor","spray":"Mancozeb"},
            {"day":28,"task":"General care","spray":"—"},
            {"day":35,"task":"Pre-harvest check","spray":"—"},
            {"day":42,"task":"—","spray":"—"},
            {"day":49,"task":"—","spray":"—"},
            {"day":56,"task":"—","spray":"—"},
            {"day":63,"task":"—","spray":"—"},
            {"day":70,"task":"—","spray":"—"}
        ],
        "pest_notes":["Leaf miners and fungal spots occasionally occur."],
        "rotation":[{"year":1,"crop":"রোষ্টকার্ট"},{"year":2,"crop":"ধান / ভুট্টা"},{"year":3,"crop":"ডাল"},{"year":4,"crop":"শাক"}],
        "cost":15000,
        "sell_rate":28
    },

    "পটেটো": {
        "seed_rate":"১৫০–২০০ কেজি/হেক্টর (প্রতি বিঘা ভিন্ন)",
        "expected_yield":"১০০০–১৫০০ কেজি/বিঘা",
        "yield_per_bigha":1200,
        "fertilizer":{"Base":{"Urea (kg)":30,"TSP (kg)":25,"MOP (kg)":20}},
        "spray_schedule":[
            {"day":7,"task":"Early blight prevention","spray":"Fungicide per label"},
            {"day":14,"task":"Aphid check","spray":"Imidacloprid"},
            {"day":21,"task":"Fungal follow-up","spray":"Mancozeb"},
            {"day":28,"task":"Late blight monitor","spray":"Ridomil"},
            {"day":35,"task":"General care","spray":"—"},
            {"day":42,"task":"Insect check","spray":"—"},
            {"day":49,"task":"Pre-harvest","spray":"—"},
            {"day":56,"task":"Soil health","spray":"—"},
            {"day":63,"task":"—","spray":"—"},
            {"day":70,"task":"Field sanitation","spray":"—"}
        ],
        "pest_notes":["Late blight is critical; use certified seed and fungicide rotation."],
        "rotation":[{"year":1,"crop":"পটেটো"},{"year":2,"crop":"ধান / ভুট্টা"},{"year":3,"crop":"ডাল"},{"year":4,"crop":"শাক"}],
        "cost":32000,
        "sell_rate":22
    },

    "পেয়াজ": {
        "seed_rate":"বিভিন্ন (বালপুর্বক)",
        "expected_yield":"বিভিন্ন",
        "yield_per_bigha":800,
        "fertilizer":{"Base":{"Urea (kg)":20,"TSP (kg)":20,"MOP (kg)":10}},
        "spray_schedule":[
            {"day":7,"task":"Initial care","spray":"—"},
            {"day":14,"task":"Thrips / onion fly check","spray":"Appropriate insecticide"},
            {"day":21,"task":"Fungal monitor","spray":"Mancozeb"},
            {"day":28,"task":"General care","spray":"—"},
            {"day":35,"task":"Pre-harvest","spray":"—"},
            {"day":42,"task":"—","spray":"—"},
            {"day":49,"task":"—","spray":"—"},
            {"day":56,"task":"—","spray":"—"},
            {"day":63,"task":"—","spray":"—"},
            {"day":70,"task":"—","spray":"—"}
        ],
        "pest_notes":["Onion fly and thrips can reduce yield."],
        "rotation":[{"year":1,"crop":"পেয়াজ"},{"year":2,"crop":"ধান / ভুট্টা"},{"year":3,"crop":"শাক"}],
        "cost":20000,
        "sell_rate":30
    },

    "টমেটো (গ্রীনহাউস)": {
        "seed_rate":"৩০–৪০ গ্রাম/বিঘা (গ্রীনহাউস ভিত্তিক)",
        "expected_yield":"১৫০০–২৫০০ কেজি/বিঘা",
        "yield_per_bigha":1800,
        "fertilizer":{"Base":{"Urea (kg)":30,"TSP (kg)":25,"MOP (kg)":20}},
        "spray_schedule":[
            {"day":7,"task":"Seedling care","spray":"Preventive"},
            {"day":14,"task":"Fungal check","spray":"Amistar Top"},
            {"day":21,"task":"Borer control","spray":"Spinosad"},
            {"day":28,"task":"Whitefly control","spray":"Imidacloprid"},
            {"day":35,"task":"Mid season care","spray":"—"},
            {"day":42,"task":"Bacterial check","spray":"Copper salts"},
            {"day":49,"task":"Pre-harvest","spray":"—"},
            {"day":56,"task":"Sanitation","spray":"—"},
            {"day":63,"task":"—","spray":"—"},
            {"day":70,"task":"Final check","spray":"—"}
        ],
        "pest_notes":["Greenhouse cultivation needs strict sanitation and integrated pest management."],
        "rotation":[{"year":1,"crop":"টমেটো (গ্রীনহাউস)"},{"year":2,"crop":"ক্যাপসিকাম / শসা"}],
        "cost":90000,
        "sell_rate":60
    },

    "মটর / শিম": {
        "seed_rate":"৫০০ গ্রাম–১ কেজি/বিঘা",
        "expected_yield":"৭০০–১০০০ কেজি/বিঘা",
        "yield_per_bigha":800,
        "fertilizer":{"Base":{"Urea (kg)":10,"TSP (kg)":15,"MOP (kg)":8}},
        "spray_schedule":[
            {"day":7,"task":"Initial check","spray":"—"},
            {"day":14,"task":"Aphid/bean fly check","spray":"Imidacloprid"},
            {"day":21,"task":"Fungal check","spray":"Mancozeb"},
            {"day":28,"task":"—","spray":"—"},
            {"day":35,"task":"—","spray":"—"},
            {"day":42,"task":"—","spray":"—"},
            {"day":49,"task":"—","spray":"—"},
            {"day":56,"task":"—","spray":"—"},
            {"day":63,"task":"—","spray":"—"},
            {"day":70,"task":"—","spray":"—"}
        ],
        "pest_notes":["Use rhizobium inoculant for better yield."],
        "rotation":[{"year":1,"crop":"মটর/শিম"},{"year":2,"crop":"ধান / ভুট্টা"},{"year":3,"crop":"শসা"}],
        "cost":18000,
        "sell_rate":55
    }
}
