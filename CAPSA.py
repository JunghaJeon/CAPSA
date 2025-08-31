"""
CAPSA MVP 시스템 구조 설계 (Pythonic Pseudo-code & 시스템 다이어그램 설명)

1. 전체 구조 개요
-----------------
- **Admin CMS**: 관리자만 접근 가능한 백엔드 대시보드. Job/Announcement CRUD, Stakeholder 요청 관리.
- **Public Job Board**: 누구나 열람 가능한 채용공고 리스트. Apply 클릭 시 외부 URL로 리다이렉트.
- **Stakeholder Hub**: 전문가/멘토/엔젤 연결 요청 폼. 제출 시 관리자에게 알림 및 DB/스프레드시트 저장.
- **Community Bulletin**: 커뮤니티 공지/이벤트/뉴스 게시판. 관리자만 글 작성/수정/삭제/핀 고정.

2. 데이터 흐름 및 관리자 워크플로우
-------------------------------
- 모든 콘텐츠(채용, 공지, 요청)는 관리자에 의해 수동으로 입력/큐레이션됨.
- Stakeholder 요청은 폼 제출 → DB/스프레드시트 저장 → 관리자 이메일 알림 → 수동 매칭 및 상태 업데이트.
- Job/Announcement는 관리자 CMS에서 CRUD, 공개 페이지ㅔ에 실시간 반영.
- Apply/Request Intro 등 사용자의 액션은 외부 URL 리다이렉트 또는 폼 제출(데이터 저장/이메일 알림).

3. 시스템 다이어그램 (텍스트 기반)
-------------------------------
[User/Visitor]
    │
    ├──> [Public Job Board] <─── [Admin CMS] <─── [Admin]
    │           │
    │           └─(Apply 클릭)─> [외부 회사 채용 페이지]
    │
    ├──> [Stakeholder Hub]
    │           │
    │           └─(Request Intro 폼 제출)─> [DB/스프레드시트 저장] + [Admin 이메일 알림]
    │
    └──> [Community Bulletin] <─── [Admin CMS] <─── [Admin]
"""

from datetime import datetime

# 데이터 모델 (간단 예시)
class JobPost:
    def __init__(self, title, company, location, apply_url, description, posted_at):
        self.title = title
        self.company = company
        self.location = location
        self.apply_url = apply_url
        self.description = description
        self.posted_at = posted_at

class StakeholderRequest:
    def __init__(self, name, email, company, role, help_type, description, submitted_at, status="Pending"):
        self.name = name
        self.email = email
        self.company = company
        self.role = role
        self.help_type = help_type
        self.description = description
        self.submitted_at = submitted_at
        self.status = status  # Pending, In Progress, Completed

class Announcement:
    def __init__(self, title, content, pinned=False, posted_at=None):
        self.title = title
        self.content = content
        self.pinned = pinned
        self.posted_at = posted_at

# 관리자 CMS (수동 큐레이션)
class AdminCMS:
    def __init__(self):
        self.job_posts = []
        self.announcements = []
        self.stakeholder_requests = []

    # Job CRUD
    def create_job(self, job_post):
        self.job_posts.append(job_post)
    def update_job(self, idx, job_post):
        self.job_posts[idx] = job_post
    def delete_job(self, idx):
        del self.job_posts[idx]

    # Announcement CRUD
    def create_announcement(self, announcement):
        self.announcements.append(announcement)
    def update_announcement(self, idx, announcement):
        self.announcements[idx] = announcement
    def delete_announcement(self, idx):
        del self.announcements[idx]
    def pin_announcement(self, idx, pinned=True):
        self.announcements[idx].pinned = pinned

    # Stakeholder Request 관리
    def receive_stakeholder_request(self, request):
        self.stakeholder_requests.append(request)
        self.notify_admin(request)

    def notify_admin(self, request):
        # 실제 구현에서는 이메일 발송
        print(f"[알림] 새로운 Stakeholder 요청: {request.name}, {request.email}")

    def update_request_status(self, idx, status):
        self.stakeholder_requests[idx].status = status

# 공개 Job Board (필터/검색 포함)
def public_job_board(job_posts, filters=None):
    # filters: {'location': 'US', 'role': 'PM'}
    filtered = []
    for job in job_posts:
        match = True
        if filters:
            for k, v in filters.items():
                if getattr(job, k, None) != v:
                    match = False
        if match:
            filtered.append(job)
    # 카드 형태로 출력 (실제 구현은 프론트엔드)
    for job in filtered:
        print(f"{job.title} @ {job.company} ({job.location}) - [Apply]({job.apply_url})")

# Stakeholder Hub (Request Intro 폼)
def stakeholder_hub_submit(cms, name, email, company, role, help_type, description):
    req = StakeholderRequest(
        name, email, company, role, help_type, description, submitted_at=datetime.now()
    )
    cms.receive_stakeholder_request(req)
    print("요청이 접수되었습니다. 확인 이메일을 곧 받게 됩니다.")

# Community Bulletin (공지/이벤트)
def public_bulletin(announcements):
    # 핀된 글 먼저, 그 다음 최신순
    pinned = [a for a in announcements if a.pinned]
    others = sorted([a for a in announcements if not a.pinned], key=lambda x: x.posted_at, reverse=True)
    for a in pinned + others:
        print(f"{'[PINNED] ' if a.pinned else ''}{a.title} - {a.posted_at}")

# ============================================================================
# 실행 가능한 데모 코드
# ============================================================================

if __name__ == "__main__":
    print("🚀 CAPSA MVP 시스템 데모 시작")
    print("=" * 50)
    
    # CMS 인스턴스 생성
    cms = AdminCMS()
    
    # 샘플 데이터 생성
    print("\n📝 샘플 데이터 생성 중...")
    
    # Job Posts 생성
    job1 = JobPost("Senior Product Manager", "TechCorp", "San Francisco", "https://techcorp.com/careers", "혁신적인 제품을 만들어보세요", "2024-01-15")
    job2 = JobPost("Frontend Developer", "StartupXYZ", "Seoul", "https://startupxyz.com/jobs", "React/Next.js 개발자 모집", "2024-01-16")
    job3 = JobPost("Data Scientist", "AI Company", "Remote", "https://aico.com/careers", "머신러닝 모델 개발", "2024-01-17")
    
    cms.create_job(job1)
    cms.create_job(job2)
    cms.create_job(job3)
    
    # Announcements 생성
    ann1 = Announcement("커뮤니티 가이드라인 업데이트", "새로운 커뮤니티 규칙이 적용되었습니다.", pinned=True, posted_at=datetime.now())
    ann2 = Announcement("월간 네트워킹 이벤트", "1월 25일 온라인 네트워킹 이벤트를 개최합니다.", pinned=False, posted_at=datetime.now())
    
    cms.create_announcement(ann1)
    cms.create_announcement(ann2)
    
    # Stakeholder Requests 생성
    req1 = StakeholderRequest("김멘토", "mentor@example.com", "대기업", "Senior Manager", "Career Advice", "커리어 전환에 대한 조언이 필요합니다", datetime.now())
    req2 = StakeholderRequest("박엔젤", "angel@example.com", "벤처캐피탈", "Partner", "Investment", "스타트업 투자에 관심이 있습니다", datetime.now())
    
    cms.receive_stakeholder_request(req1)
    cms.receive_stakeholder_request(req2)
    
    print("✅ 샘플 데이터 생성 완료!")
    
    # ============================================================================
    # 시스템 기능 데모
    # ============================================================================
    
    print("\n" + "=" * 50)
    print("📋 1. 공개 Job Board")
    print("=" * 50)
    public_job_board(cms.job_posts)
    
    print("\n" + "=" * 50)
    print("🔍 2. Job Board 필터링 (위치: Seoul)")
    print("=" * 50)
    public_job_board(cms.job_posts, filters={'location': 'Seoul'})
    
    print("\n" + "=" * 50)
    print("📢 3. Community Bulletin")
    print("=" * 50)
    public_bulletin(cms.announcements)
    
    print("\n" + "=" * 50)
    print("👥 4. Stakeholder Requests 현황")
    print("=" * 50)
    for i, req in enumerate(cms.stakeholder_requests):
        print(f"[{i+1}] {req.name} ({req.company}) - {req.help_type}: {req.status}")
    
    print("\n" + "=" * 50)
    print("🔄 5. Request 상태 업데이트")
    print("=" * 50)
    cms.update_request_status(0, "In Progress")
    print("김멘토의 요청 상태를 'In Progress'로 업데이트했습니다.")
    
    print("\n" + "=" * 50)
    print("📝 6. 새로운 Stakeholder 요청 제출")
    print("=" * 50)
    stakeholder_hub_submit(cms, "이전문가", "expert@example.com", "컨설팅회사", "Principal", "Mentoring", "스타트업 멘토링을 제공하고 싶습니다")
    
    print("\n" + "=" * 50)
    print("🎯 7. 최종 시스템 상태")
    print("=" * 50)
    print(f"총 Job Posts: {len(cms.job_posts)}개")
    print(f"총 Announcements: {len(cms.announcements)}개")
    print(f"총 Stakeholder Requests: {len(cms.stakeholder_requests)}개")
    
    print("\n" + "=" * 50)
    print("✨ CAPSA MVP 시스템 데모 완료!")
    print("=" * 50)

