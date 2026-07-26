from services.ai_service import AIService

try:
    result = AIService.analyze_resume(
        "Python Flask SQL Machine Learning",
        "Looking for Python Flask SQL Developer"
    )
    print("\n✅ API Call Successful! Here is the JSON output:\n")
    print(result)
except Exception as e:
    print("\n❌ Error:", e)