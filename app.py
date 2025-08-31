from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'capsa-secret-key-2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///capsa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 데이터베이스 모델
class JobPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    apply_url = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text, nullable=False)
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)

class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    pinned = db.Column(db.Boolean, default=False)
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)

class StakeholderRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    help_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default='Pending')

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# 데이터베이스 생성
with app.app_context():
    db.create_all()
    
    # 기본 관리자 계정 생성 (없는 경우)
    if not Admin.query.filter_by(username='admin').first():
        admin = Admin(username='admin', password='admin123')
        db.session.add(admin)
        db.session.commit()

# 라우트
@app.route('/')
def home():
    jobs = JobPost.query.order_by(JobPost.posted_at.desc()).limit(6).all()
    announcements = Announcement.query.filter_by(pinned=True).all()
    return render_template('home.html', jobs=jobs, announcements=announcements)

@app.route('/jobs')
def jobs():
    location = request.args.get('location', '')
    if location:
        jobs = JobPost.query.filter(JobPost.location.contains(location)).order_by(JobPost.posted_at.desc()).all()
    else:
        jobs = JobPost.query.order_by(JobPost.posted_at.desc()).all()
    return render_template('jobs.html', jobs=jobs, location=location)

@app.route('/stakeholder-hub', methods=['GET', 'POST'])
def stakeholder_hub():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        company = request.form['company']
        role = request.form['role']
        help_type = request.form['help_type']
        description = request.form['description']
        
        request_obj = StakeholderRequest(
            name=name, email=email, company=company, 
            role=role, help_type=help_type, description=description
        )
        db.session.add(request_obj)
        db.session.commit()
        
        flash('요청이 성공적으로 제출되었습니다!', 'success')
        return redirect(url_for('stakeholder_hub'))
    
    return render_template('stakeholder_hub.html')

@app.route('/community')
def community():
    announcements = Announcement.query.order_by(Announcement.pinned.desc(), Announcement.posted_at.desc()).all()
    return render_template('community.html', announcements=announcements)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        admin = Admin.query.filter_by(username=username, password=password).first()
        if admin:
            session['admin'] = True
            flash('관리자로 로그인되었습니다.', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('잘못된 로그인 정보입니다.', 'error')
    
    return render_template('admin_login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('admin'):
        return redirect(url_for('admin_login'))
    
    jobs = JobPost.query.order_by(JobPost.posted_at.desc()).all()
    announcements = Announcement.query.order_by(Announcement.posted_at.desc()).all()
    requests = StakeholderRequest.query.order_by(StakeholderRequest.submitted_at.desc()).all()
    
    return render_template('admin_dashboard.html', jobs=jobs, announcements=announcements, requests=requests)

@app.route('/admin/job/add', methods=['GET', 'POST'])
def add_job():
    if not session.get('admin'):
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        job = JobPost(
            title=request.form['title'],
            company=request.form['company'],
            location=request.form['location'],
            apply_url=request.form['apply_url'],
            description=request.form['description']
        )
        db.session.add(job)
        db.session.commit()
        flash('채용공고가 추가되었습니다.', 'success')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('add_job.html')

@app.route('/admin/announcement/add', methods=['GET', 'POST'])
def add_announcement():
    if not session.get('admin'):
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        announcement = Announcement(
            title=request.form['title'],
            content=request.form['content'],
            pinned=bool(request.form.get('pinned'))
        )
        db.session.add(announcement)
        db.session.commit()
        flash('공지사항이 추가되었습니다.', 'success')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('add_announcement.html')

@app.route('/admin/request/<int:request_id>/update', methods=['POST'])
def update_request_status(request_id):
    if not session.get('admin'):
        return redirect(url_for('admin_login'))
    
    request_obj = StakeholderRequest.query.get_or_404(request_id)
    request_obj.status = request.form['status']
    db.session.commit()
    flash('요청 상태가 업데이트되었습니다.', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin', None)
    flash('로그아웃되었습니다.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
