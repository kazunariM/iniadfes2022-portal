import datetime


# 事前登録期日
PREREGISTRATION = datetime.date(2022, 10, 26)


# 二次元コード読み取りインターバル
CAMPUSQR_INTERVAL = 3 * 60
ROOMQR_INTERVAL = 10


ADDRESS_CHOICES = [
    (1, "東京都（北区）"),
    (2, "東京都（23区）"),
    (3, "東京都（市部）"),
    (4, "埼玉県（川口）"),
    (5, "埼玉県（）"),
    (6, "神奈川県"),
    (7, "茨城県"),
    (8, "栃木県"),
    (9, "群馬県"),
    (10, "千葉県"),
    (11, "北海道"),
    (12, "青森県"),
    (13, "岩手県"),
    (14, "宮城県"),
    (15, "秋田県"),
    (16, "山形県"),
    (17, "福島県"),
    (18, "新潟県"),
    (19, "富山県"),
    (20, "石川県"),
    (21, "福井県"),
    (22, "山梨県"),
    (23, "長野県"),
    (24, "岐阜県"),
    (25, "静岡県"),
    (26, "愛知県"),
    (27, "三重県"),
    (28, "滋賀県"),
    (29, "京都府"),
    (30, "大阪府"),
    (31, "兵庫県"),
    (32, "奈良県"),
    (33, "和歌山県"),
    (34, "鳥取県"),
    (35, "島根県"),
    (36, "岡山県"),
    (37, "広島県"),
    (38, "山口県"),
    (39, "徳島県"),
    (40, "香川県"),
    (41, "愛媛県"),
    (42, "高知県"),
    (43, "福岡県"),
    (44, "佐賀県"),
    (45, "長崎県"),
    (46, "熊本県"),
    (47, "大分県"),
    (48, "宮崎県"),
    (49, "鹿児島県"),
    (50, "沖縄県"),
]

JOB_CHOICES = [
    (1, "未就学児"),
    (2, "小学生"),
    (3, "中学生"),
    (4, "高校生"),
    (5, "大学生"),
    (6, "その他の学生"),
    (7, "会社員"),
    (8, "教職員"),
    (9, "自営業"),
    (10, "その他"),
]

AGE_CHOICES = [
    (0, "10歳未満"),
    (1, "10代"),
    (2, "20代"),
    (3, "30代"),
    (4, "40代"),
    (5, "50代"),
    (6, "60代"),
    (7, "70代"),
    (8, "80歳以上"),
]

GENDER_CHOICES = [
    (1, "男性"),
    (2, "女性"),
    (3, "その他"),
    (4, "指定しない"),
]

MAJOR_SUBJECT_CHOICES = [
    (1, "情報系"),
    (2, "理系"),
    (3, "文系"),
    (4, "その他"),
]
