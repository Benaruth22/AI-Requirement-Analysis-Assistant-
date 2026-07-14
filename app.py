from utils.parser import extract_text_from_pdf
from utils.analyzer import analyze_requirements

def main():
    print("📄 AI Requirement Analysis Assistant")
    srs_file = "sample_srs.pdf"  # Replace with your own SRS document

    # Step 1: Extract text
    print("Extracting text from SRS...")
    srs_text = extract_text_from_pdf(srs_file)

    # Step 2: Analyze with LLM
    print("Analyzing requirements with AI...")
    analysis_result = analyze_requirements(srs_text)

    # Step 3: Save output
    output_file = "outputs/generated_report.txt"
    with open(output_file, "w") as f:
        f.write(analysis_result)

    print(f"✅ Analysis complete! Results saved to {output_file}")

if __name__ == "__main__":
    main()