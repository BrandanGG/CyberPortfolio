# Security Portfolio Website

A security-focused portfolio website built with Flask, featuring a dark theme and comprehensive security implementations.

## Security Features

### Security Headers
- **Content Security Policy (CSP)**: Prevents XSS attacks by controlling resource loading
- **Strict Transport Security (HSTS)**: Enforces HTTPS connections
- **X-Frame-Options**: Prevents clickjacking attacks
- **X-Content-Type-Options**: Prevents MIME type sniffing
- **X-XSS-Protection**: Enables browser XSS filtering
- **Referrer-Policy**: Controls referrer information leakage

### Secure Configuration
- Debug mode disabled in production
- Secure session configuration
- Input validation and sanitization
- Minimal JavaScript for reduced attack surface
- No external dependencies for enhanced security

## Tech Stack

### Frontend
- **HTML5**: Semantic markup with security considerations
- **CSS3**: Dark theme with security-focused design
- **JavaScript**: Minimal JS for enhanced security

### Backend
- **Python Flask**: Lightweight WSGI framework
- **Security Headers**: Comprehensive security header implementation
- **Template Engine**: Jinja2 with auto-escaping

### Infrastructure
- **Docker**: Containerized deployment
- **Alpine Linux**: Minimal attack surface
- **Nginx**: Reverse proxy with SSL termination (recommended)

## Sections

1. **About Me**: Security background and skills
2. **Certificates & Education**: Professional certifications and education
3. **Homelab**: Network topology and security infrastructure
4. **Tech Stack**: This website's technology stack and security implementations

## Running the Application

### Development
```bash
python3 app.py
```

### Production with Gunicorn
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Docker
```bash
docker build -t security-portfolio .
docker run -p 8000:8000 security-portfolio
```

## Security Best Practices Implemented

1. **Defense in Depth**: Multiple layers of security controls
2. **Principle of Least Privilege**: Minimal permissions and dependencies
3. **Secure by Default**: Security headers and configurations
4. **Input Validation**: Proper sanitization and validation
5. **Error Handling**: Secure error messages without information leakage

## Customization

To customize the portfolio:

1. **Personal Information**: Update the content in `templates/index.html`
2. **Certificates**: Modify the certificates section with your credentials
3. **Homelab**: Update the network topology and features
4. **Styling**: Customize colors and fonts in `static/css/style.css`

## Security Considerations

- Always run behind a reverse proxy (Nginx) with SSL/TLS
- Regularly update dependencies
- Monitor for security vulnerabilities
- Implement proper logging and monitoring
- Use environment variables for sensitive configuration
