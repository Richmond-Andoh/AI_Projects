from career_expert_system.knowledge_base import knowledge_base;

def recommend_career(user_interest, user_skills, user_education):
    recommendations = []
    for rule in knowledge_base:
        if rule["interest"] == user_interest and all(skill in user_skills for skill in rule["skills"]):
            if rule["education"] == user_education or rule["education"] == "any":
                recommendations.append(rule["career"])
    
    return recommendations if recommendations else ["No matching careers found."]

