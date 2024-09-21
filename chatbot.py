from patan_hospital_data import hospital_info

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
                return self.info["facilities"].get("emergency")
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
            elif "cafeteria" in query or "food" in query:
                return self.info["facility"].get("cafeteria")
            elif "billing" in query:
                return self.info["facility"].get("billing")
            elif "admission" in query:
                return self.info["facility"].get("admission")
            elif "discharge" in query:
                return self.info["facility"].get("discharge")
            elif "ambulance" in query:
                return self.info["facility"].get("ambulance")
            elif "covid vaccination" in query or "vaccination" in query:
                return self.info["facility"].get("covid_vaccination")
            elif "testing lab" in query or "lab" in query:
                return self.info["facility"].get("testing_lab")
            else:
                return "Please specify the facility you're asking about."
        elif "visiting hours" in query or "visit" in query:
            if "icu" in query:
                return self.info["visiting_hours"].get("icu")
            elif "maternity" in query:
                return self.info["visiting_hours"].get("maternity")
            else:
                return self.info["visiting_hours"].get("general")
        elif "appointment" in query or "book" in query or "process" in query:
            if "booking" in query or "book" in query:
                return self.info["appointment"].get("booking")
            elif "cancellation" in query:
                return self.info["appointment"].get("cancellation")
            elif "online" in query:
                return self.info["appointment"].get("online")
            else:
                return self.info["appointment"].get("overview", "Please specify the appointment-related query.")
        else:
            return "I'm sorry, I don't have information on that. Please contact the hospital directly."

# Example usage

chatbot = PatanHelper()
print("Welcome to PatanHelper! How can I assist you with Patan Hospital information?")

while True:
    user_query = input("You: ")
    if user_query.lower() in ["exit", "quit"]:
        print("Thank you for using PatanHelper. Stay healthy!")
        break
    response = chatbot.respond(user_query)
    print(f"PatanHelper: {response}")
