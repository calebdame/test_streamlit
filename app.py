import streamlit as st
from streamlit_javascript import st_javascript


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


ip_address = client_ip()  # now you have it in the host...

st.write(ip_address)  # so you can log it, etc.
