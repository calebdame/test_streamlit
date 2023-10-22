import streamlit as st
from streamlit_javascript import st_javascript

if len(st.session_state) == 0:
    st.session_state["ip"] = []
    st.session_state["uas"] = []
    

def client_ip():

    url = 'https://api.ipify.org?format=json'

    script = (f'await fetch("{url}").then('
                'function(response) {'
                    'return response.json();'
                '})')

    try:
        result = st_javascript(script)

        if isinstance(result, dict) and 'ip' in result:
            return result['ip']

    except:
        pass

def get_user_agent():

    script = ('navigator.userAgent')

    try:
        user_agent = st_javascript(script)
        if user_agent:
            return user_agent
    except:
        pass

user_agent_str = get_user_agent()
st.session_state["uas"].append(user_agent_str)
st.write(f"User-Agent: {user_agent_str}")  # Log the user-agent string

ip_address = client_ip()  # now you have it in the host...

st.session_state["ip"].append(ip_address)
st.write(ip_address)  # so you can log it, etc.

st.write(st.session_state)
