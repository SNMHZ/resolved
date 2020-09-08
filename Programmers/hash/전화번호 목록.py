#https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    m_data = {}
    
    phone_book.sort(key=len, reverse=True)
    st_index=len(phone_book[-1])-1
    
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            m_data[ phone_book[i][:len(phone_book[j])] ]=0
            if phone_book[j] in m_data:
                return False
    
    return True