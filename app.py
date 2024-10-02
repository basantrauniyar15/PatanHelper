from flask import Flask, render_template, request, jsonify

hospital_info = {
    "general_info": "Patan Hospital is a major healthcare institution located in Kathmandu, Nepal. It provides comprehensive medical services across various departments and is known for its quality care and experienced medical professionals. The hospital offers a range of services including emergency care, outpatient and inpatient services, specialized surgeries, diagnostics, and more. It is easily accessible, with facilities such as parking, a 24/7 pharmacy, and a cafeteria for patients and visitors.",
    "location": {
        "address": "Patan Hospital is located at Lagankhel, Lalitpur, Kathmandu.",
        "direction": "The hospital is easily accessible by public transport. It is near the Lagankhel bus park, and taxis are readily available in the area. View it on Google Maps here: https://maps.app.goo.gl/HBCKpGkytq2mhN6z5",
        "parking": "Parking is provided on-site for patients and visitors at the hospital."
    },
    "emergency_ward": {
        "overview": "The emergency ward is on the ground floor of the main building, accessible directly from the main entrance. The Emergency Department is operational 24/7 and is staffed with experienced medical personnel ready to handle all types of emergencies.",
        "location": "The emergency ward is on the ground floor of the main building, accessible directly from the main entrance. View the hospital's location on Google Maps: https://maps.app.goo.gl/HBCKpGkytq2mhN6z5",
        "ambulance": "Ambulance services are available 24/7. To request an ambulance, call 01-5522295.",
        "trauma_care": "We have a dedicated trauma care unit equipped to handle severe injuries and emergencies."
    },
    "contact": {
        "general": "For general inquiries, please contact the hospital reception at 01-5522295.",
        "appointments": "To book an appointment, please call the appointment desk at 01-5522295 or visit the hospital in person.",
        "emergency": "In case of an emergency, call 01-5522295 or visit the Emergency Department directly."
    },
    "departments": {
        "general": "Patan Hospital has various departments, including Cardiology, Neurology, Orthopedics, Pediatrics, Gynecology, ENT, and more.",
        "doctors": {
            "general_physicians": "Our team of general physicians provides comprehensive care for a variety of health conditions. Appointments can be made for consultations.",
            "specialists": "We have specialists in cardiology, neurology, gastroenterology, orthopedics, and more. Each specialist is available for consultation on specific days.",
            "surgeons": "Patan Hospital has experienced surgeons in general surgery, orthopedic surgery, and other specialized areas.",
            "pediatricians": "Our pediatricians are experts in child healthcare, offering both outpatient and inpatient services.",
            "gynecologists": "Our gynecology department provides a range of services including prenatal care, childbirth, and reproductive health.",
            "doctor": "Physicians, Specialists, Surgeons, Pediatricians, and many more."
        }
    },
    "facility": {
        "outpatient": "The hospital has outpatient departments (OPD) for general medicine, surgery, pediatrics, orthopedics, and more. OPD hours are from 9 AM to 4 PM on weekdays.",
        "inpatient": "Patan Hospital provides inpatient care with well-equipped wards and private rooms. Services include general care, intensive care, and maternity wards.",
        "emergency": "The Emergency Department is operational 24/7 and is staffed with experienced medical personnel ready to handle all types of emergencies.",
        "surgery": "The hospital offers surgical services including general surgery, orthopedic surgery, and specialized procedures. The surgical department is equipped with modern operating rooms.",
        "diagnostics": "Patan Hospital has a fully equipped diagnostic center offering lab services, imaging (X-ray, MRI, CT scan), and other diagnostic tests.",
        "pharmacy": "The hospital's pharmacy is open 24/7, providing a wide range of medications and health supplies.",
        "cafeteria": "There is a cafeteria on the hospital premises that offers food and beverages to visitors and patients.",
        "billing": "Billing counters are located on the ground floor near the main entrance. You can pay your bills here or inquire about insurance.",
        "admission": "For admission procedures, please visit the admission desk on the ground floor near the main entrance.",
        "discharge": "The discharge process can be initiated by visiting the discharge desk, which is located near the billing counters.",
        "ambulance": "Patan Hospital provides ambulance services. You can request an ambulance by calling the hospital's emergency contact number.",
        "covid_vaccination": "Patan Hospital is a designated COVID-19 vaccination center. Vaccination services are provided in a separate building within the hospital premises.",
        "testing_lab": "The hospital has a well-equipped testing lab for various medical tests. The lab is located on the first floor."
    },
    "visiting_hours": {
        "general": "Visiting hours for most wards are from 9 AM to 6 PM. For ICU and special wards, visiting hours may vary. Please check with the ward staff.",
        "icu": "ICU visiting hours are limited to 30 minutes in the morning and evening. Only immediate family members are allowed.",
        "maternity": "Visiting hours for the maternity ward are from 3 PM to 5 PM. Special permissions may be granted for fathers or close relatives."
    },
    "appointment": {
        "booking": "Appointments can be booked by calling the hospital at 01-5522295. You can also visit the hospital and book an appointment in person.",
        "cancellation": "To cancel an appointment, please contact the appointment desk at least 24 hours in advance.",
        "online": "Online appointment booking is currently unavailable. Please use phone or in-person booking options."
    }
}


class PatanHelper:
    def __init__(self):
        self.info = hospital_info

    def respond(self, query):
        query = query.lower()

        if query in ["hi", "hello", "hey"]:
            return "Hello! How can I assist you with Patan Hospital information today?"
        if query in ["thank you", "thanks", "thankyou"]:
            return "You're welcome! If you have any more questions, feel free to ask."

        if "general information" in query or "info" in query or "history" in query:
            return self.info.get("general_info")
        elif "location" in query or "reach" in query or "direction" in query or "parking" in query:
            if "direction" in query or "how to reach" in query or "reach" in query:
                return self.info["location"].get("direction")
            elif "parking" in query:
                return self.info["location"].get("parking")
            else:
                return self.info["location"].get("address")
        elif "emergency" in query or "ambulance" in query:
            if "ward" in query or "location" in query:
                return self.info["emergency_ward"].get("location")
            elif "services" in query:
                return self.info["facility"].get("emergency")
            elif "ambulance" in query:
                return self.info["emergency_ward"].get("ambulance")
            elif "trauma" in query:
                return self.info["emergency_ward"].get("trauma_care")
            else:
                return self.info["emergency_ward"].get("overview")
        elif "contact" in query or "phone" in query:
            if "appointment" in query:
                return self.info["contact"].get("appointments")
            elif "urgent" in query:
                return self.info["contact"].get("emergency")
            else:
                return self.info["contact"].get("general")
        elif "departments" in query:
            return self.info["departments"].get("general")
        elif "doctors" in query or "physicians" in query or "specialists" in query or "surgeons" in query or "gynecologists" in query or "pediatricians" in query:
            if "general" in query or "physicians" in query:
                return self.info["departments"]["doctors"].get("general_physicians")
            elif "specialists" in query:
                return self.info["departments"]["doctors"].get("specialists")
            elif "surgeons" in query:
                return self.info["departments"]["doctors"].get("surgeons")
            elif "pediatricians" in query:
                return self.info["departments"]["doctors"].get("pediatricians")
            elif "gynecologists" in query:
                return self.info["departments"]["doctors"].get("gynecologists")
            else:
                return self.info["departments"]["doctors"]
        elif "facility" in query or "service" in query:
            if "outpatient" in query:
                return self.info["facility"].get("outpatient")
            elif "inpatient" in query:
                return self.info["facility"].get("inpatient")
            elif "surgery" in query:
                return self.info["facility"].get("surgery")
            elif "diagnostics" in query:
                return self.info["facility"].get("diagnostics")
            elif "pharmacy" in query:
                return self.info["facility"].get("pharmacy")
            elif "cafeteria" in query:
                return self.info["facility"].get("cafeteria")
            elif "billing" in query:
                return self.info["facility"].get("billing")
            elif "admission" in query:
                return self.info["facility"].get("admission")
            elif "discharge" in query:
                return self.info["facility"].get("discharge")
            elif "covid" in query:
                return self.info["facility"].get("covid_vaccination")
            elif "testing" in query:
                return self.info["facility"].get("testing_lab")
            else:
                return self.info["facility"].get("overview")
        elif "visiting hours" in query:
            return self.info["visiting_hours"].get("general")
        elif "appointment" in query:
            if "book" in query:
                return self.info["appointment"].get("booking")
            elif "cancel" in query:
                return self.info["appointment"].get("cancellation")
            elif "online" in query:
                return self.info["appointment"].get("online")
            else:
                return self.info["appointment"].get("overview")
        else:
            return "I'm sorry, I didn't quite understand that. Can you please rephrase your question?"

app = Flask(__name__)
chatbot = PatanHelper()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.form["message"]
    bot_response = chatbot.respond(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
