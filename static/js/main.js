// CAPSA 웹사이트 메인 JavaScript 파일

// 페이지 로드 시 실행
document.addEventListener('DOMContentLoaded', function() {
    initializeWebsite();
});

// 웹사이트 초기화
function initializeWebsite() {
    // 스크롤 애니메이션 초기화
    initializeScrollAnimations();
    
    // 네비게이션 활성 상태 설정
    setActiveNavigation();
    
    // 로딩 스피너 제거
    removeLoadingSpinner();
    
    // 콘솔 로그
    console.log('🚀 CAPSA 웹사이트가 로드되었습니다!');
}

// 스크롤 애니메이션 초기화
function initializeScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                entry.target.classList.add('revealed');
            }
        });
    }, observerOptions);
    
    // 애니메이션 대상 요소들
    const animatedElements = document.querySelectorAll(
        '.feature-card, .job-card, .announcement-card, .event-card, .guideline-item, .stat-item'
    );
    
    animatedElements.forEach(el => {
        observer.observe(el);
    });
}

// 네비게이션 활성 상태 설정
function setActiveNavigation() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath || 
            (currentPath === '/' && href === '/') ||
            (currentPath.startsWith('/admin') && href.includes('admin'))) {
            link.classList.add('active');
        }
    });
}

// 로딩 스피너 제거
function removeLoadingSpinner() {
    const spinner = document.querySelector('.loading-spinner');
    if (spinner) {
        spinner.style.opacity = '0';
        setTimeout(() => {
            spinner.remove();
        }, 300);
    }
}

// 스크롤 상단 이동 버튼
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// 스크롤 상단 이동 버튼 표시/숨김
window.addEventListener('scroll', function() {
    const scrollTopBtn = document.getElementById('scrollTopBtn');
    if (scrollTopBtn) {
        if (window.pageYOffset > 300) {
            scrollTopBtn.style.display = 'block';
        } else {
            scrollTopBtn.style.display = 'none';
        }
    }
});

// 모바일 메뉴 토글
function toggleMobileMenu() {
    const navbarCollapse = document.querySelector('.navbar-collapse');
    if (navbarCollapse) {
        navbarCollapse.classList.toggle('show');
    }
}

// 검색 기능
function performSearch(query) {
    if (query.trim()) {
        // 채용정보 페이지로 검색어와 함께 이동
        window.location.href = `/jobs?search=${encodeURIComponent(query.trim())}`;
    }
}

// 검색 폼 제출 처리
document.addEventListener('submit', function(e) {
    if (e.target.classList.contains('search-form')) {
        e.preventDefault();
        const searchInput = e.target.querySelector('input[name="search"]');
        if (searchInput) {
            performSearch(searchInput.value);
        }
    }
});

// 카드 호버 효과
function initializeCardHoverEffects() {
    const cards = document.querySelectorAll('.card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 10px 25px rgba(0,0,0,0.15)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
        });
    });
}

// 알림 메시지 자동 숨김
function initializeAlertAutoHide() {
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(alert => {
        if (!alert.classList.contains('alert-persistent')) {
            setTimeout(() => {
                alert.style.opacity = '0';
                setTimeout(() => {
                    alert.remove();
                }, 300);
            }, 5000); // 5초 후 자동 숨김
        }
    });
}

// 폼 유효성 검사 강화
function initializeFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = this.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    field.classList.add('is-invalid');
                    isValid = false;
                } else {
                    field.classList.remove('is-invalid');
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                showNotification('필수 항목을 모두 입력해주세요.', 'error');
            }
        });
    });
}

// 알림 메시지 표시
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // 3초 후 자동 제거
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// 로컬 스토리지 유틸리티
const Storage = {
    set: function(key, value) {
        try {
            localStorage.setItem(key, JSON.stringify(value));
            return true;
        } catch (e) {
            console.error('로컬 스토리지 저장 실패:', e);
            return false;
        }
    },
    
    get: function(key, defaultValue = null) {
        try {
            const item = localStorage.getItem(key);
            return item ? JSON.parse(item) : defaultValue;
        } catch (e) {
            console.error('로컬 스토리지 읽기 실패:', e);
            return defaultValue;
        }
    },
    
    remove: function(key) {
        try {
            localStorage.removeItem(key);
            return true;
        } catch (e) {
            console.error('로컬 스토리지 삭제 실패:', e);
            return false;
        }
    }
};

// 사용자 설정 저장
function saveUserPreferences() {
    const preferences = {
        theme: document.body.classList.contains('dark-theme') ? 'dark' : 'light',
        notifications: Storage.get('notifications', true),
        language: Storage.get('language', 'ko')
    };
    
    Storage.set('userPreferences', preferences);
}

// 사용자 설정 불러오기
function loadUserPreferences() {
    const preferences = Storage.get('userPreferences', {});
    
    if (preferences.theme === 'dark') {
        document.body.classList.add('dark-theme');
    }
    
    // 기타 설정들 적용
    if (preferences.notifications !== undefined) {
        // 알림 설정 적용
    }
}

// 페이지 가시성 변경 감지
document.addEventListener('visibilitychange', function() {
    if (document.hidden) {
        // 페이지가 숨겨질 때
        document.title = '👋 CAPSA - 돌아와주세요!';
    } else {
        // 페이지가 다시 보일 때
        document.title = 'CAPSA - 커리어 & 네트워킹 플랫폼';
    }
});

// 오프라인 상태 감지
window.addEventListener('online', function() {
    showNotification('인터넷 연결이 복구되었습니다.', 'success');
});

window.addEventListener('offline', function() {
    showNotification('인터넷 연결이 끊어졌습니다.', 'warning');
});

// 성능 모니터링
function measurePageLoadTime() {
    window.addEventListener('load', function() {
        const loadTime = performance.now();
        console.log(`📊 페이지 로드 시간: ${loadTime.toFixed(2)}ms`);
        
        // 성능 데이터를 분석 서비스로 전송 (선택사항)
        if (loadTime > 3000) {
            console.warn('⚠️ 페이지 로드 시간이 3초를 초과했습니다.');
        }
    });
}

// 초기화 함수들 실행
document.addEventListener('DOMContentLoaded', function() {
    initializeCardHoverEffects();
    initializeAlertAutoHide();
    initializeFormValidation();
    loadUserPreferences();
    measurePageLoadTime();
});

// 전역 함수로 노출
window.CAPSA = {
    showNotification,
    Storage,
    scrollToTop,
    performSearch
};
