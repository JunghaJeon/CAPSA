#!/usr/bin/env python3
"""
간단한 정적 사이트 생성기
GitHub Pages 배포용
"""

import os
import shutil
from datetime import datetime

def create_static_site():
    """정적 사이트 생성"""
    
    # docs 폴더 생성 (GitHub Pages용)
    docs_dir = 'docs'
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
    os.makedirs(docs_dir)
    
    # static 폴더 복사
    if os.path.exists('static'):
        shutil.copytree('static', os.path.join(docs_dir, 'static'))
    
    # 샘플 데이터
    sample_jobs = [
        {
            'id': 1,
            'title': '시니어 백엔드 개발자',
            'company': '테크스타트업 A',
            'location': '서울 강남구',
            'job_type': '정규직',
            'description': 'Python/Django 기반 백엔드 시스템 개발 및 운영을 담당합니다.',
            'requirements': '• Python 5년 이상 경험\n• Django/Flask 프레임워크 숙련\n• AWS 클라우드 경험\n• 데이터베이스 설계 경험',
            'created_at': '2024-08-31'
        },
        {
            'id': 2,
            'title': '프론트엔드 개발자',
            'company': '디지털 에이전시 B',
            'location': '서울 마포구',
            'job_type': '계약직',
            'description': 'React 기반 웹 애플리케이션 개발 및 UI/UX 구현을 담당합니다.',
            'requirements': '• React 3년 이상 경험\n• TypeScript 숙련\n• 반응형 웹 개발 경험\n• Git 협업 경험',
            'created_at': '2024-08-30'
        },
        {
            'id': 3,
            'title': '데이터 사이언티스트',
            'company': '핀테크 스타트업 C',
            'location': '서울 송파구',
            'job_type': '정규직',
            'description': '금융 데이터 분석 및 머신러닝 모델 개발을 담당합니다.',
            'requirements': '• Python 데이터 분석 3년 이상\n• 머신러닝/딥러닝 경험\n• SQL 숙련\n• 금융 도메인 이해',
            'created_at': '2024-08-29'
        }
    ]
    
    sample_announcements = [
        {
            'id': 1,
            'title': 'CAPSA 플랫폼 오픈 베타 시작!',
            'content': '안녕하세요! CAPSA 플랫폼의 오픈 베타가 시작되었습니다. 많은 관심과 참여 부탁드립니다.',
            'author': 'CAPSA 운영팀',
            'created_at': '2024-08-31'
        },
        {
            'id': 2,
            'title': '첫 번째 네트워킹 이벤트 개최',
            'content': '9월 15일 강남에서 첫 번째 오프라인 네트워킹 이벤트를 개최합니다. 많은 참여 바랍니다!',
            'author': '이벤트팀',
            'created_at': '2024-08-30'
        },
        {
            'id': 3,
            'title': '전문가 멘토링 프로그램 런칭',
            'content': '경력 개발을 위한 1:1 멘토링 프로그램이 시작됩니다. 신청은 전문가 연결 메뉴에서 가능합니다.',
            'author': '서비스팀',
            'created_at': '2024-08-29'
        }
    ]
    
    # 기본 HTML 템플릿
    base_template = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="./static/css/style.css" rel="stylesheet">
</head>
<body>
    <!-- 네비게이션 바 -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand fw-bold" href="./index.html">
                <i class="fas fa-network-wired me-2"></i>CAPSA
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="./index.html">홈</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./jobs.html">채용정보</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./stakeholder-hub.html">전문가 연결</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./community.html">커뮤니티</a>
                    </li>
                </ul>
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="#" onclick="alert('데모 사이트입니다. 실제 로그인은 로컬에서만 가능합니다.')">
                            <i class="fas fa-user-shield me-1"></i>관리자
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- 메인 콘텐츠 -->
    <main class="py-4">
        {content}
    </main>

    <!-- 푸터 -->
    <footer class="bg-dark text-light py-4 mt-5">
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <h5><i class="fas fa-network-wired me-2"></i>CAPSA</h5>
                    <p class="mb-0">커리어와 네트워킹의 새로운 시작</p>
                </div>
                <div class="col-md-6 text-md-end">
                    <p class="mb-0">&copy; 2024 CAPSA. All rights reserved.</p>
                    <small>GitHub Pages로 배포된 데모 사이트입니다.</small>
                </div>
            </div>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="./static/js/main.js"></script>
</body>
</html>"""

    # 홈페이지 생성
    home_content = """
    <div class="hero-section bg-primary text-white py-5">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <h1 class="display-4 fw-bold mb-4">
                        커리어와 네트워킹의<br>
                        <span class="text-warning">새로운 시작</span>
                    </h1>
                    <p class="lead mb-4">
                        CAPSA에서 당신의 꿈을 현실로 만들어보세요.<br>
                        전문가와의 연결, 최신 채용정보, 그리고 활발한 커뮤니티가 기다립니다.
                    </p>
                    <div class="d-flex gap-3">
                        <a href="./jobs.html" class="btn btn-warning btn-lg">
                            <i class="fas fa-briefcase me-2"></i>채용정보 보기
                        </a>
                        <a href="./stakeholder-hub.html" class="btn btn-outline-light btn-lg">
                            <i class="fas fa-handshake me-2"></i>전문가 연결
                        </a>
                    </div>
                </div>
                <div class="col-lg-6 text-center">
                    <i class="fas fa-rocket" style="font-size: 8rem; opacity: 0.8;"></i>
                </div>
            </div>
        </div>
    </div>

    <div class="container my-5">
        <!-- 주요 기능 -->
        <section class="mb-5">
            <h2 class="text-center mb-5">
                <i class="fas fa-star text-warning me-2"></i>주요 기능
            </h2>
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="feature-card text-center h-100 p-4 border rounded-3 shadow-sm">
                        <div class="feature-icon text-primary mb-3">
                            <i class="fas fa-briefcase" style="font-size: 3rem;"></i>
                        </div>
                        <h4>채용정보</h4>
                        <p>최신 채용공고와 맞춤형 일자리 추천을 받아보세요.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card text-center h-100 p-4 border rounded-3 shadow-sm">
                        <div class="feature-icon text-success mb-3">
                            <i class="fas fa-handshake" style="font-size: 3rem;"></i>
                        </div>
                        <h4>전문가 연결</h4>
                        <p>업계 전문가와 직접 연결되어 조언과 멘토링을 받으세요.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card text-center h-100 p-4 border rounded-3 shadow-sm">
                        <div class="feature-icon text-info mb-3">
                            <i class="fas fa-users" style="font-size: 3rem;"></i>
                        </div>
                        <h4>커뮤니티</h4>
                        <p>동료들과 정보를 공유하고 네트워킹을 확장하세요.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 최신 채용정보 -->
        <section class="mb-5">
            <div class="d-flex justify-content-between align-items-center mb-4">
                <h3><i class="fas fa-briefcase text-primary me-2"></i>최신 채용정보</h3>
                <a href="./jobs.html" class="btn btn-outline-primary">전체보기</a>
            </div>
            <div class="row g-4">
                <div class="col-md-6">
                    <div class="job-card border rounded-3 p-4 shadow-sm h-100">
                        <div class="d-flex justify-content-between align-items-start mb-3">
                            <h5 class="mb-0">시니어 백엔드 개발자</h5>
                            <span class="badge bg-success">정규직</span>
                        </div>
                        <p class="text-muted mb-2">
                            <i class="fas fa-building me-1"></i>테크스타트업 A
                            <span class="mx-2">•</span>
                            <i class="fas fa-map-marker-alt me-1"></i>서울 강남구
                        </p>
                        <p class="mb-3">Python/Django 기반 백엔드 시스템 개발 및 운영을 담당합니다.</p>
                        <small class="text-muted">2024-08-31</small>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="job-card border rounded-3 p-4 shadow-sm h-100">
                        <div class="d-flex justify-content-between align-items-start mb-3">
                            <h5 class="mb-0">프론트엔드 개발자</h5>
                            <span class="badge bg-info">계약직</span>
                        </div>
                        <p class="text-muted mb-2">
                            <i class="fas fa-building me-1"></i>디지털 에이전시 B
                            <span class="mx-2">•</span>
                            <i class="fas fa-map-marker-alt me-1"></i>서울 마포구
                        </p>
                        <p class="mb-3">React 기반 웹 애플리케이션 개발 및 UI/UX 구현을 담당합니다.</p>
                        <small class="text-muted">2024-08-30</small>
                    </div>
                </div>
            </div>
        </section>

        <!-- 커뮤니티 공지 -->
        <section class="mb-5">
            <div class="d-flex justify-content-between align-items-center mb-4">
                <h3><i class="fas fa-bullhorn text-success me-2"></i>커뮤니티 소식</h3>
                <a href="./community.html" class="btn btn-outline-success">전체보기</a>
            </div>
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="announcement-card border rounded-3 p-4 shadow-sm h-100">
                        <h6 class="fw-bold mb-2">CAPSA 플랫폼 오픈 베타 시작!</h6>
                        <p class="small mb-2">안녕하세요! CAPSA 플랫폼의 오픈 베타가 시작되었습니다...</p>
                        <small class="text-muted">CAPSA 운영팀 • 2024-08-31</small>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="announcement-card border rounded-3 p-4 shadow-sm h-100">
                        <h6 class="fw-bold mb-2">첫 번째 네트워킹 이벤트 개최</h6>
                        <p class="small mb-2">9월 15일 강남에서 첫 번째 오프라인 네트워킹 이벤트를...</p>
                        <small class="text-muted">이벤트팀 • 2024-08-30</small>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="announcement-card border rounded-3 p-4 shadow-sm h-100">
                        <h6 class="fw-bold mb-2">전문가 멘토링 프로그램 런칭</h6>
                        <p class="small mb-2">경력 개발을 위한 1:1 멘토링 프로그램이 시작됩니다...</p>
                        <small class="text-muted">서비스팀 • 2024-08-29</small>
                    </div>
                </div>
            </div>
        </section>

        <!-- CTA 섹션 -->
        <section class="text-center py-5 bg-light rounded-3">
            <h3 class="mb-4">지금 바로 시작하세요!</h3>
            <p class="lead mb-4">CAPSA와 함께 새로운 기회를 발견하고 전문가와 연결되세요.</p>
            <div class="d-flex justify-content-center gap-3">
                <a href="./stakeholder-hub.html" class="btn btn-primary btn-lg">
                    <i class="fas fa-rocket me-2"></i>전문가 연결 신청
                </a>
                <a href="./jobs.html" class="btn btn-outline-primary btn-lg">
                    <i class="fas fa-search me-2"></i>채용정보 탐색
                </a>
            </div>
        </section>
    </div>"""
    
    # 채용정보 페이지 콘텐츠
    jobs_content = f"""
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h1 class="mb-4">
                    <i class="fas fa-briefcase text-primary me-2"></i>채용정보
                </h1>
                
                <!-- 검색 및 필터 -->
                <div class="card mb-4">
                    <div class="card-body">
                        <div class="row g-3">
                            <div class="col-md-4">
                                <input type="text" class="form-control" placeholder="제목, 회사명 검색..." id="searchInput">
                            </div>
                            <div class="col-md-3">
                                <select class="form-select" id="locationFilter">
                                    <option value="">전체 지역</option>
                                    <option value="서울">서울</option>
                                    <option value="경기">경기</option>
                                    <option value="부산">부산</option>
                                </select>
                            </div>
                            <div class="col-md-3">
                                <select class="form-select" id="typeFilter">
                                    <option value="">전체 고용형태</option>
                                    <option value="정규직">정규직</option>
                                    <option value="계약직">계약직</option>
                                    <option value="프리랜서">프리랜서</option>
                                </select>
                            </div>
                            <div class="col-md-2">
                                <button class="btn btn-primary w-100" onclick="filterJobs()">
                                    <i class="fas fa-search"></i> 검색
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 채용정보 목록 -->
                <div class="row g-4" id="jobsList">
                    {"".join([f'''
                    <div class="col-md-6 job-item" data-location="{job['location']}" data-type="{job['job_type']}">
                        <div class="job-card border rounded-3 p-4 shadow-sm h-100">
                            <div class="d-flex justify-content-between align-items-start mb-3">
                                <h5 class="mb-0">{job['title']}</h5>
                                <span class="badge bg-{'success' if job['job_type'] == '정규직' else 'info'}">{job['job_type']}</span>
                            </div>
                            <p class="text-muted mb-3">
                                <i class="fas fa-building me-1"></i>{job['company']}
                                <span class="mx-2">•</span>
                                <i class="fas fa-map-marker-alt me-1"></i>{job['location']}
                            </p>
                            <p class="mb-3">{job['description']}</p>
                            <div class="mb-3">
                                <h6>주요 요구사항:</h6>
                                <small class="text-muted">{job['requirements'].replace(chr(10), '<br>')}</small>
                            </div>
                            <div class="d-flex justify-content-between align-items-center">
                                <small class="text-muted">
                                    <i class="fas fa-calendar me-1"></i>{job['created_at']}
                                </small>
                                <div class="btn-group" role="group">
                                    <button class="btn btn-outline-primary btn-sm" onclick="alert('데모 사이트입니다.')">
                                        <i class="fas fa-heart me-1"></i>저장
                                    </button>
                                    <button class="btn btn-outline-secondary btn-sm" onclick="alert('데모 사이트입니다.')">
                                        <i class="fas fa-share me-1"></i>공유
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    ''' for job in sample_jobs])}
                </div>
            </div>
        </div>
    </div>

    <script>
        function filterJobs() {{
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const locationFilter = document.getElementById('locationFilter').value;
            const typeFilter = document.getElementById('typeFilter').value;
            const jobItems = document.querySelectorAll('.job-item');
            
            jobItems.forEach(item => {{
                const title = item.querySelector('h5').textContent.toLowerCase();
                const company = item.querySelector('.fa-building').parentNode.textContent.toLowerCase();
                const location = item.dataset.location;
                const type = item.dataset.type;
                
                const matchesSearch = title.includes(searchTerm) || company.includes(searchTerm);
                const matchesLocation = !locationFilter || location.includes(locationFilter);
                const matchesType = !typeFilter || type === typeFilter;
                
                if (matchesSearch && matchesLocation && matchesType) {{
                    item.style.display = 'block';
                }} else {{
                    item.style.display = 'none';
                }}
            }});
        }}
    </script>"""

    # 전문가 연결 페이지 콘텐츠
    stakeholder_content = """
    <div class="container">
        <div class="row">
            <div class="col-lg-8 mx-auto">
                <h1 class="mb-4 text-center">
                    <i class="fas fa-handshake text-success me-2"></i>전문가 연결
                </h1>
                
                <div class="alert alert-info mb-4">
                    <h5><i class="fas fa-info-circle me-2"></i>전문가 연결 서비스란?</h5>
                    <p class="mb-0">업계 전문가와 직접 연결되어 커리어 조언, 기술 멘토링, 비즈니스 인사이트를 얻을 수 있는 서비스입니다.</p>
                </div>

                <div class="card shadow">
                    <div class="card-header bg-success text-white">
                        <h5 class="mb-0"><i class="fas fa-user-plus me-2"></i>연결 요청서 작성</h5>
                    </div>
                    <div class="card-body">
                        <div class="alert alert-warning">
                            <i class="fas fa-exclamation-triangle me-2"></i>
                            <strong>데모 사이트 안내:</strong> 실제 요청 제출은 로컬 환경에서만 가능합니다.
                        </div>
                        
                        <form id="stakeholderForm" onsubmit="handleDemoSubmit(event)">
                            <div class="row g-3">
                                <div class="col-md-6">
                                    <label for="name" class="form-label">이름 *</label>
                                    <input type="text" class="form-control" id="name" required>
                                </div>
                                <div class="col-md-6">
                                    <label for="email" class="form-label">이메일 *</label>
                                    <input type="email" class="form-control" id="email" required>
                                </div>
                                <div class="col-md-6">
                                    <label for="company" class="form-label">소속 회사/기관 *</label>
                                    <input type="text" class="form-control" id="company" required>
                                </div>
                                <div class="col-md-6">
                                    <label for="position" class="form-label">직책/포지션 *</label>
                                    <input type="text" class="form-control" id="position" required>
                                </div>
                                <div class="col-12">
                                    <label for="expertise_area" class="form-label">관심 전문 분야 *</label>
                                    <select class="form-select" id="expertise_area" required>
                                        <option value="">선택해주세요</option>
                                        <option value="기술개발">기술개발</option>
                                        <option value="제품기획">제품기획</option>
                                        <option value="마케팅">마케팅</option>
                                        <option value="영업">영업</option>
                                        <option value="인사">인사</option>
                                        <option value="재무">재무</option>
                                        <option value="법무">법무</option>
                                        <option value="기타">기타</option>
                                    </select>
                                </div>
                                <div class="col-12">
                                    <label for="request_details" class="form-label">구체적인 요청 내용 *</label>
                                    <textarea class="form-control" id="request_details" rows="5" 
                                              placeholder="어떤 도움이나 조언을 받고 싶으신지 구체적으로 작성해주세요." required></textarea>
                                </div>
                            </div>
                            
                            <div class="d-grid mt-4">
                                <button type="submit" class="btn btn-success btn-lg">
                                    <i class="fas fa-paper-plane me-2"></i>연결 요청 보내기
                                </button>
                            </div>
                        </form>
                    </div>
                </div>

                <!-- FAQ 섹션 -->
                <div class="mt-5">
                    <h4 class="mb-4"><i class="fas fa-question-circle text-info me-2"></i>자주 묻는 질문</h4>
                    <div class="accordion" id="faqAccordion">
                        <div class="accordion-item">
                            <h2 class="accordion-header">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq1">
                                    연결 요청 후 얼마나 기다려야 하나요?
                                </button>
                            </h2>
                            <div id="faq1" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
                                <div class="accordion-body">
                                    일반적으로 3-5일 내에 적합한 전문가를 매칭해드립니다. 전문 분야와 요청 내용에 따라 시간이 달라질 수 있습니다.
                                </div>
                            </div>
                        </div>
                        <div class="accordion-item">
                            <h2 class="accordion-header">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq2">
                                    비용이 발생하나요?
                                </button>
                            </h2>
                            <div id="faq2" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
                                <div class="accordion-body">
                                    기본 연결 서비스는 무료입니다. 단, 전문가와의 심화 멘토링이나 장기 컨설팅은 별도 협의가 필요할 수 있습니다.
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        function handleDemoSubmit(event) {{
            event.preventDefault();
            alert('데모 사이트입니다. 실제 서비스는 로컬 환경에서 이용해주세요!\\n\\n제출하신 정보:\\n- 이름: ' + 
                  document.getElementById('name').value + '\\n- 전문분야: ' + 
                  document.getElementById('expertise_area').value);
        }}
    </script>"""

    # 커뮤니티 페이지 콘텐츠
    community_content = f"""
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h1 class="mb-4">
                    <i class="fas fa-users text-success me-2"></i>커뮤니티
                </h1>
                
                <!-- 커뮤니티 가이드라인 -->
                <div class="alert alert-primary mb-4">
                    <h5><i class="fas fa-info-circle me-2"></i>커뮤니티 가이드라인</h5>
                    <ul class="mb-0">
                        <li>서로를 존중하며 건설적인 대화를 나누어주세요</li>
                        <li>스팸이나 광고성 게시물은 금지됩니다</li>
                        <li>개인정보 보호를 위해 민감한 정보 공유는 피해주세요</li>
                        <li>질문이나 도움 요청은 언제든 환영합니다</li>
                    </ul>
                </div>

                <!-- 공지사항 목록 -->
                <div class="d-flex justify-content-between align-items-center mb-4">
                    <h3><i class="fas fa-bullhorn text-warning me-2"></i>공지사항 및 소식</h3>
                    <span class="badge bg-secondary">{len(sample_announcements)}개의 게시물</span>
                </div>

                <div class="row g-4">
                    {"".join([f'''
                    <div class="col-12">
                        <div class="announcement-card border rounded-3 p-4 shadow-sm">
                            <div class="d-flex justify-content-between align-items-start mb-3">
                                <h5 class="mb-0">{announcement['title']}</h5>
                                <small class="text-muted">{announcement['created_at']}</small>
                            </div>
                            <p class="mb-3">{announcement['content']}</p>
                            <div class="d-flex justify-content-between align-items-center">
                                <small class="text-muted">
                                    <i class="fas fa-user me-1"></i>작성자: {announcement['author']}
                                </small>
                                <div class="btn-group" role="group">
                                    <button class="btn btn-outline-primary btn-sm" onclick="alert('데모 사이트입니다.')">
                                        <i class="fas fa-thumbs-up me-1"></i>좋아요
                                    </button>
                                    <button class="btn btn-outline-secondary btn-sm" onclick="alert('데모 사이트입니다.')">
                                        <i class="fas fa-comment me-1"></i>댓글
                                    </button>
                                    <button class="btn btn-outline-info btn-sm" onclick="alert('데모 사이트입니다.')">
                                        <i class="fas fa-share me-1"></i>공유
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    ''' for announcement in sample_announcements])}
                </div>

                <!-- 이벤트 정보 -->
                <div class="mt-5">
                    <h4 class="mb-4"><i class="fas fa-calendar-alt text-info me-2"></i>예정된 이벤트</h4>
                    <div class="row g-4">
                        <div class="col-md-6">
                            <div class="card border-info">
                                <div class="card-header bg-info text-white">
                                    <h6 class="mb-0"><i class="fas fa-calendar me-2"></i>2024년 9월 15일</h6>
                                </div>
                                <div class="card-body">
                                    <h6>첫 번째 네트워킹 이벤트</h6>
                                    <p class="small mb-2">장소: 서울 강남구 (상세 주소 추후 공지)</p>
                                    <p class="small">다양한 분야의 전문가들과 만나 네트워킹하고 인사이트를 공유하는 시간입니다.</p>
                                    <button class="btn btn-info btn-sm" onclick="alert('데모 사이트입니다.')">참가 신청</button>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="card border-warning">
                                <div class="card-header bg-warning text-dark">
                                    <h6 class="mb-0"><i class="fas fa-calendar me-2"></i>2024년 9월 22일</h6>
                                </div>
                                <div class="card-body">
                                    <h6>온라인 세미나: 커리어 전환 전략</h6>
                                    <p class="small mb-2">시간: 오후 7시 - 9시 (온라인)</p>
                                    <p class="small">성공적인 커리어 전환을 위한 실전 전략과 노하우를 공유합니다.</p>
                                    <button class="btn btn-warning btn-sm" onclick="alert('데모 사이트입니다.')">참가 신청</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        function filterJobs() {{
            // 검색 기능 구현 (데모용)
            alert('검색 기능은 로컬 환경에서 이용 가능합니다.');
        }}
    </script>"""

    # 페이지별 HTML 파일 생성
    pages = {
        'index.html': ('CAPSA - 커리어 & 네트워킹 플랫폼', home_content),
        'jobs.html': ('채용정보 - CAPSA', jobs_content),
        'stakeholder-hub.html': ('전문가 연결 - CAPSA', stakeholder_content),
        'community.html': ('커뮤니티 - CAPSA', community_content),
    }
    
    for filename, (title, content) in pages.items():
        html_content = base_template.format(title=title, content=content)
        
        with open(os.path.join(docs_dir, filename), 'w', encoding='utf-8') as f:
            f.write(html_content)
    
    print(f"✅ 정적 사이트가 {docs_dir}/ 폴더에 생성되었습니다!")
    print("📁 생성된 파일:")
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), docs_dir)
            print(f"   - {relative_path}")

if __name__ == '__main__':
    create_static_site()
