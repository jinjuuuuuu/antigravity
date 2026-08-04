# -*- coding: utf-8 -*-
"""
Supabase 데이터베이스 연동 파이썬 예제
필요 패키지 설치: pip install supabase
"""

from supabase import create_client, Client

# Supabase 프로젝트 연동 설정 (실제 적용됨)
SUPABASE_URL = "https://kpimgkffpqukrgyllron.supabase.co"
SUPABASE_KEY = "sb_publishable_TTbKKXp22l3howHI-sabFA_EWang2K5"

# Supabase 클라이언트 생성
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_bmi_to_supabase(height, weight, bmi, category):
    """
    BMI 측정 결과를 Supabase 'bmi_records' 클라우드 테이블에 저장하는 함수
    """
    data = {
        "height": height,
        "weight": weight,
        "bmi": bmi,
        "category": category
    }
    
    # bmi_records 테이블에 데이터 삽입
    response = supabase.table("bmi_records").insert(data).execute()
    print("✅ Supabase Cloud DB 저장 완료:", response)
    return response

def get_bmi_history():
    """
    Supabase Cloud DB에서 최근 10개의 BMI 기록을 조회하는 함수
    """
    response = supabase.table("bmi_records").select("*").order("created_at", desc=True).limit(10).execute()
    print("📋 최근 BMI 기록 목록:")
    for record in response.data:
        print(f"[{record['created_at'][:10]}] 키: {record['height']}cm | 몸무게: {record['weight']}kg | BMI: {record['bmi']} ({record['category']})")
    return response.data

if __name__ == "__main__":
    print("Supabase DB 연결 정보 준비 완료:", SUPABASE_URL)
