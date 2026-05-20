import streamlit as st
st.title('피카츄')
st.write('라이츄') 
import streamlit as st
from datetime import date

st.set_page_config(page_title="스케줄 관리", page_icon="📅")

st.title("📅 스케줄 관리 앱")

# 세션 상태 초기화
if "schedules" not in st.session_state:
    st.session_state.schedules = []

# 입력 영역
st.subheader("새 일정 추가")

title = st.text_input("일정 제목")
schedule_date = st.date_input("날짜", value=date.today())
memo = st.text_area("메모")

# 추가 버튼
if st.button("일정 추가"):
    if title:
        st.session_state.schedules.append({
            "title": title,
            "date": schedule_date,
            "memo": memo
        })
        st.success("일정이 추가되었습니다!")
    else:
        st.warning("일정 제목을 입력하세요.")

# 일정 목록
st.subheader("📋 일정 목록")

if st.session_state.schedules:
    for idx, item in enumerate(st.session_state.schedules):
        with st.expander(f"{item['date']} - {item['title']}"):
            st.write(f"메모: {item['memo']}")

            if st.button("삭제", key=idx):
                st.session_state.schedules.pop(idx)
                st.rerun()
else:
    st.info("등록된 일정이 없습니다.")
