import streamlit as st

# =======================
# OOP CLASSES
# =======================

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Doctor(User):
    def __init__(self, name, specialty):
        super().__init__(name, "Doctor 🩺")
        self.specialty = specialty

class Nurse(User):
    def __init__(self, name, ward):
        super().__init__(name, "Nurse 👩‍⚕️")
        self.ward = ward

class Admin(User):
    def __init__(self, name):
        super().__init__(name, "Admin 🧑‍💼")

class Patient:
    def __init__(self, name, age, illness):
        self.name = name
        self.age = age
        self.illness = illness

class Appointment:
    def __init__(self, doctor, patient, time):
        self.doctor = doctor
        self.patient = patient
        self.time = time

# =======================
# STREAMLIT APP
# =======================

# Initialize session state
if 'doctors' not in st.session_state:
    st.session_state.doctors = []

if 'nurses' not in st.session_state:
    st.session_state.nurses = []

if 'patients' not in st.session_state:
    st.session_state.patients = []

if 'appointments' not in st.session_state:
    st.session_state.appointments = []

st.title("🏥 Hospital Management System")

menu = st.sidebar.selectbox("📋 Menu", [
    "➕ Add Doctor",
    "➕ Add Nurse",
    "➕ Add Patient",
    "👨‍⚕️ View Staff",
    "📅 Schedule Appointment",
    "🗂️ View Appointments"
])

# ========== Add Doctor ==========
if menu == "➕ Add Doctor":
    st.header("🩺 Add Doctor")
    name = st.text_input("👨‍⚕️ Doctor's Name")
    specialty = st.text_input("🔬 Specialty")
    if st.button("✅ Add Doctor"):
        doc = Doctor(name, specialty)
        st.session_state.doctors.append(doc)
        st.success(f"✅ Doctor **{name}** added successfully!")

# ========== Add Nurse ==========
elif menu == "➕ Add Nurse":
    st.header("👩‍⚕️ Add Nurse")
    name = st.text_input("👩 Nurse's Name")
    ward = st.text_input("🏥 Assigned Ward")
    if st.button("✅ Add Nurse"):
        nurse = Nurse(name, ward)
        st.session_state.nurses.append(nurse)
        st.success(f"✅ Nurse **{name}** added successfully!")

# ========== Add Patient ==========
elif menu == "➕ Add Patient":
    st.header("🧑‍🦽 Add Patient")
    name = st.text_input("🧍 Patient Name")
    age = st.number_input("🎂 Age", min_value=0, step=1)
    illness = st.text_input("🤒 Illness")
    if st.button("✅ Add Patient"):
        patient = Patient(name, age, illness)
        st.session_state.patients.append(patient)
        st.success(f"✅ Patient **{name}** added successfully!")

# ========== View Staff ==========
elif menu == "👨‍⚕️ View Staff":
    st.header("🩺 Doctors List")
    if st.session_state.doctors:
        for doc in st.session_state.doctors:
            st.write(f"- 👨‍⚕️ Dr. **{doc.name}**, Specialty: _{doc.specialty}_")
    else:
        st.warning("⚠️ No doctors added yet.")

    st.header("👩‍⚕️ Nurses List")
    if st.session_state.nurses:
        for nurse in st.session_state.nurses:
            st.write(f"- 👩‍⚕️ Nurse **{nurse.name}**, Ward: _{nurse.ward}_")
    else:
        st.warning("⚠️ No nurses added yet.")

# ========== Schedule Appointment ==========
elif menu == "📅 Schedule Appointment":
    st.header("📅 Schedule New Appointment")
    if not st.session_state.doctors or not st.session_state.patients:
        st.warning("⚠️ Please add at least one doctor and one patient first.")
    else:
        doc_names = [f"Dr. {doc.name}" for doc in st.session_state.doctors]
        pat_names = [p.name for p in st.session_state.patients]

        selected_doc = st.selectbox("👨‍⚕️ Select Doctor", doc_names)
        selected_pat = st.selectbox("🧍 Select Patient", pat_names)
        time = st.time_input("⏰ Appointment Time")

        if st.button("✅ Schedule Appointment"):
            doc_obj = next(doc for doc in st.session_state.doctors if f"Dr. {doc.name}" == selected_doc)
            pat_obj = next(p for p in st.session_state.patients if p.name == selected_pat)
            app = Appointment(doc_obj, pat_obj, time)
            st.session_state.appointments.append(app)
            st.success(f"✅ Appointment scheduled for **{pat_obj.name}** with **{selected_doc}** at **{time}**")

# ========== View Appointments ==========
elif menu == "🗂️ View Appointments":
    st.header("📋 Scheduled Appointments")
    if st.session_state.appointments:
        for app in st.session_state.appointments:
            st.write(
                f"🧍 **{app.patient.name}** with 👨‍⚕️ Dr. **{app.doctor.name}** (_{app.doctor.specialty}_) at ⏰ {app.time}"
            )
    else:
        st.warning("⚠️ No appointments scheduled yet.")
