import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-june-2023-default-rtdb.firebaseio.com/"
})

ref = db.reference('DnHFaces')

data = {
    "01":
        {
            "name": "ab_gp_0_eo_25.JPG",
            "detection_no": 1

        },
    "02":
        {
            "name": "cd_gp_3_eo_25.JPG",
            "detection_no": 2
        },
    "03":
        {
            "name": "ef_gp_0_eo_27.JPG",
            "detection_no": 3
        },
    "04":
        {
            "name": "gh_gp_0_eo_29.JPG",
            "detection_no": 1
        },
    "05":
        {
            "name": "ijk_gp_0_eo_30.JPG",
            "detection_no": 0
        },
    "06":
        {
            "name": "Saif_Ali",
            "detection_no": 3
        },
    "07":
        {
            "name": "Rohit Kumar",
            "detection_no": 1
        },
    "08":
        {
            "name": "Pratynsh_J_Deka",
            "detection_no": 3
        },
    "09":
        {
            "name": "Saurabh_kumar",
            "detection_no": 4
        },
    "10":
        {
            "name": "Rahul Thakur",
            "detection_no": 2
        },
    "11":
        {
            "name": "Saksam Som",
            "detection_no": 1
        },
    "12":
        {
            "name": "Rahul Kr Sharma",
            "detection_no": 2
        },
    "13":
        {
            "name": "Vikrant Kumar",
            "detection_no": 2
        },
    "14":
        {
            "name": "Santanu Ghose",
            "detection_no": 1
        },
    "15":
        {
            "name": "Nabojyoti Nath",
            "detection_no": 2
        },
    "16":
        {
            "name": "Ravi Raj",
            "detection_no": 3
        },
    "17":
        {
            "name": "Anand Raj",
            "detection_no": 1
        },
    "18":
        {
            "name": "Ramavtar Toshi",
            "detection_no": 2
        },
    "19":
        {
            "name": "Rishav_Sheivastaur",
            "detection_no": 1
        },
    "20":
        {
            "name": "Md Aziz",
            "detection_no": 2
        },

}

for key, value in data.items():
    ref.child(key).set(value)
