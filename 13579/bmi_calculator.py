# -*- coding: utf-8 -*-
"""
BMI (체질량지수) 계산기 파이썬 프로그램
작성 폴더: 13579/
"""

def calculate_bmi(height_cm, weight_kg):
    """
    키(cm)와 몸무게(kg)를 받아 BMI 수치를 계산하는 함수입니다.
    공식: 몸무게(kg) / (키(m) * 키(m))
    """
    # 1. cm 단위의 키를 m 단위로 변환합니다. (예: 175cm -> 1.75m)
    height_m = height_cm / 100
    
    # 2. BMI = 몸무게 / (키 * 키)
    bmi = weight_kg / (height_m ** 2)
    
    # 3. 소수점 둘째 자리까지 반올림하여 반환합니다.
    return round(bmi, 2)

def get_bmi_category(bmi):
    """
    계산된 BMI 수치에 따른 비만도 판정 기준 (대한비만학회 기준)
    """
    if bmi < 18.5:
        return "저체중"
    elif 18.5 <= bmi < 23.0:
        return "정상"
    elif 23.0 <= bmi < 25.0:
        return "과체중 (비만 전단계)"
    elif 25.0 <= bmi < 30.0:
        return "1단계 비만"
    else:
        return "2단계 이상 고도비만"

def main():
    print("=" * 40)
    print("        📊 BMI 체질량지수 계산기")
    print("=" * 40)
    
    try:
        # 사용자로부터 키와 몸무게 입력받기
        height_cm = float(input("키를 입력하세요 (cm 단위, 예: 175): "))
        weight_kg = float(input("몸무게를 입력하세요 (kg 단위, 예: 70): "))
        
        # 입력값 유효성 검사
        if height_cm <= 0 or weight_kg <= 0:
            print("❌ 키와 몸무게는 0보다 큰 숫자를 입력해야 합니다.")
            return

        # BMI 계산 및 판정
        bmi = calculate_bmi(height_cm, weight_kg)
        category = get_bmi_category(bmi)

        # 결과 출력
        print("\n" + "-" * 40)
        print(f"📏 입력한 키      : {height_cm} cm ({height_cm/100:.2f} m)")
        print(f"⚖️ 입력한 몸무게  : {weight_kg} kg")
        print(f"💡 계산된 BMI 수치: {bmi}")
        print(f"📌 비만도 판정    : {category}")
        print("-" * 40)

    except ValueError:
        print("❌ 숫자 형태로 정확히 입력해 주세요. (예: 170.5, 65)")

if __name__ == "__main__":
    main()
