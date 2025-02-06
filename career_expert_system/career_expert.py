from experta import *

class CareerExpert(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        """Initial action to start the inference engine."""
        yield Fact(action="career_recommendation")

    # Technology Careers
    @Rule(Fact(action="career_recommendation"),
          Fact(interest="technology"),
          Fact(skill="programming"),
          Fact(education="bachelor"))
    def software_dev(self):
        self.declare(Fact(career="Software Developer"))

    @Rule(Fact(action="career_recommendation"),
          Fact(interest="technology"),
          Fact(skill="AI, machine learning"),
          Fact(education="master"))
    def ai_engineer(self):
        self.declare(Fact(career="AI Engineer"))

    @Rule(Fact(action="career_recommendation"),
          Fact(interest="technology"),
          Fact(skill="cybersecurity"),
          Fact(education="bachelor"))
    def cybersecurity_analyst(self):
        self.declare(Fact(career="Cybersecurity Analyst"))

    # Healthcare Careers
    @Rule(Fact(action="career_recommendation"),
          Fact(interest="healthcare"),
          Fact(skill="patient care"),
          Fact(education="associate"))
    def nurse(self):
        self.declare(Fact(career="Nurse"))

    @Rule(Fact(action="career_recommendation"),
          Fact(interest="healthcare"),
          Fact(skill="surgery"),
          Fact(education="doctorate"))
    def surgeon(self):
        self.declare(Fact(career="Surgeon"))

    # Business & Finance Careers
    @Rule(Fact(action="career_recommendation"),
          Fact(interest="finance"),
          Fact(skill="investment analysis"),
          Fact(education="bachelor"))
    def financial_analyst(self):
        self.declare(Fact(career="Financial Analyst"))

    @Rule(Fact(action="career_recommendation"),
          Fact(interest="finance"),
          Fact(skill="accounting"),
          Fact(education="bachelor"))
    def accountant(self):
        self.declare(Fact(career="Accountant"))

    # Creative & Education Careers
    @Rule(Fact(action="career_recommendation"),
          Fact(interest="education"),
          Fact(skill="communication"),
          Fact(education="bachelor"))
    def teacher(self):
        self.declare(Fact(career="Teacher"))

    @Rule(Fact(action="career_recommendation"),
          Fact(interest="art"),
          Fact(skill="design"))
    def graphic_designer(self):
        self.declare(Fact(career="Graphic Designer"))

    # No match case
    @Rule(Fact(action="career_recommendation"),
          NOT(Fact(career=MATCH.career)))
    def no_match(self):
        """Handles cases where no career matches the user input."""
        self.declare(Fact(career="No exact match found. Consider broadening your skills!"))

    def recommend(self, interest, skill, education):
        """Runs the expert system and returns career recommendations."""
        self.reset()
        self.declare(Fact(interest=interest))
        self.declare(Fact(skill=skill))
        self.declare(Fact(education=education))
        self.run()

        return list({fact["career"] for fact in self.facts.values() if "career" in fact})
