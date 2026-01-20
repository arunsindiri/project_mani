# Digital Daily Progress Reporting (DPR) Management System

---

## 🧱 Project Idea Overview

### Current Situation
- Supervisors write Daily Progress Reports (DPR) manually on paper
- DPR pages are captured as photos
- Photos are sent via WhatsApp

### Issues Faced by Project Manager (Mani)
- Scrolling through multiple chats
- Downloading image files daily
- Difficulty reading handwritten reports
- No structured or searchable data
- Manual tracking of project progress

➡️ This process is messy, slow, and error-prone.

---

## 💡 Proposed Solution

A **cross-platform application (Mobile + PC)** where:

- Supervisors enter DPR digitally at the end of each day
- Data is sent directly to the Project Manager’s application
- Daily data is stored date-wise in a database
- Project Manager can:
  - View DPR anytime
  - Track multiple sites
  - Download DPR in Excel format

All information becomes **online, structured, searchable, and secure**.

---

## 🔷 Project Title

**Digital Daily Progress Reporting (DPR) Management System**

---

## 🎯 Project Objective

To design and develop a cross-platform application that digitizes the Daily Progress Report (DPR) process by allowing site supervisors to submit daily work updates online and enabling project managers to monitor, store, and export project data efficiently.

---

## 🧠 Problem Statement

Currently, Daily Progress Reports are recorded manually on paper and shared through photographs via WhatsApp. This method results in:

- Data loss
- Poor readability
- Lack of centralized storage
- No historical tracking
- Time-consuming monitoring process

The proposed system eliminates manual reporting and introduces a centralized digital platform for efficient daily project monitoring.

---

## 📱 Platform Specifications

### Application Type
- Cross-platform application

### Supported Platforms
- Android (Mobile)
- Windows / Linux (PC)

Single codebase deployment.

---

## 👥 User Roles

### 1️⃣ Supervisor
- Secure login
- Select assigned site
- Enter DPR details:
  - Date
  - Work completed
  - Materials used
  - Number of workers
  - Remarks
- Submit DPR at end of day
- View submitted DPR history

### 2️⃣ Project Manager (Mani)
- Secure login
- View DPR from all sites
- Filter reports by:
  - Date
  - Site
  - Supervisor
- View historical DPR data
- Download DPR in Excel format

---

## 🧩 Functional Specifications

### 🔹 Supervisor Module
- Login authentication
- DPR data entry form
- Daily submission validation
- Upload data to server
- History viewing option

### 🔹 Manager Module
- Dashboard interface
- Site-wise DPR listing
- Daily summary view
- Search and filter functionality
- Excel download feature

### 🔹 Database Module
- SQLite database
- Stores:
  - User details
  - Supervisor information
  - Site information
  - Daily DPR records
- Date-wise structured storage
- Optional offline data storage

### 🔹 Export Module
- Generate Excel (.xlsx) files
- Auto-format DPR data
- Download to local device

---

## 🧰 Software Specifications

### Programming Language
- Python

### Backend Framework
- Flask or FastAPI

### Frontend Options

**Option 1: Flutter**
- Mobile + Desktop app
- Modern UI

**Option 2: Streamlit (Recommended)**
- Web-based interface
- Works on mobile and PC browsers
- Easy deployment

➡️ Final Choice: **Streamlit + Flask + SQLite**

### Libraries Used
- sqlite3
- pandas
- openpyxl
- flask
- streamlit
- datetime

---

## 💾 Database Specifications

### SQLite Tables
- Users
- Sites
- DPR_Reports
- Materials
- Workers

### DPR Report Fields
- Date
- Site ID
- Supervisor ID
- Work description
- Material details
- Worker count
- Remarks

---

## ⚙️ Hardware Specifications

### Minimum Requirements
- RAM: 4 GB
- Storage: 10 GB free space
- Internet connection
- Android smartphone

### Recommended
- RAM: 8 GB or above
- Stable internet connection

---

## 🔐 Non-Functional Specifications

- User-friendly interface
- Secure login system
- Fast report submission
- Reliable data storage
- Easy Excel generation
- Scalable architecture

---

## 🚧 Constraints

- SQLite suitable for small to medium-scale usage
- Internet required for real-time synchronization
- No real-time GPS tracking (can be added later)

---

## 🚀 Future Enhancements

- Site photo upload support
- PDF report generation
- Cloud database integration (PostgreSQL / MySQL)
- Role-based access control
- Automatic WhatsApp / Email summary
- Graphical progress and analytics dashboard

---

## 🎓 Project Category

- Real-time application
- Management system
- Industry-oriented software project

---

## 🧠 Project Strengths

- Solves a real-world industry problem
- Reduces manual paperwork
- Improves accuracy and efficiency
- Easy to demonstrate during viva
- Strong addition to resume and portfolio

---

**Document prepared for GitHub repository documentation.**

