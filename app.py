import streamlit as st
from streamlit import server
from urllib.parse import parse_qs
import requests

def log_info():
    """Capture and log information."""
    ctx = server.context
    if ctx:
        # Check if 'args' are available in the query string
        args = parse_qs(ctx.request.query)
        ip = args.get('ip', [''])[0]
        user_agent = args.get('user_agent', [''])[0]
        st.write(f"Logged IP: {ip}")
        st.write(f"Logged User-Agent: {user_agent}")

st.title('Capture and Log Client Info')

# Add JavaScript to capture the client info
st.markdown(
    """
    <script>
        async function fetchInfo() {
            // Fetch public IP
            const ipResponse = await fetch('https://api.ipify.org?format=json');
            const ipData = await ipResponse.json();
            const ip = ipData.ip;

            // Get User Agent
            const userAgent = navigator.userAgent;

            // Construct the GET request URL
            const url = `/log_info?ip=${ip}&user_agent=${encodeURIComponent(userAgent)}`;

            // Send GET request to Streamlit backend
            fetch(url);
        }
        fetchInfo();
    </script>
    """,
    unsafe_allow_html=True,
)

# Log the info in Streamlit
log_info()

# Other Streamlit content
st.write('This is a test page.')
