mkdir -p ~/.app/
echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.app/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.app/config.toml
