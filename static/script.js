const roleInput = document.getElementById("role");
const jobDesc = document.getElementById("job_desc");

roleInput.addEventListener("input", () => {
  let role = roleInput.value.toLowerCase();

  if (role.includes("frontend")) {
    jobDesc.value = "We are looking for a Frontend Developer with skills in HTML, CSS, JavaScript, React, and UI/UX design.";
  
  } else if (role.includes("backend")) {
    jobDesc.value = "We are looking for a Backend Developer with skills in Python, APIs, databases, and server-side logic.";
  
  } else if (role.includes("data")) {
    jobDesc.value = "We are looking for a Data Analyst with skills in SQL, Data Analysis, Excel, and visualization tools.";
  
  } else if (
    role.includes("machine learning") ||
    role.includes("ml") ||
    role.includes("ai")
  ) {
    jobDesc.value = "We are looking for a Machine Learning Engineer with skills in Python, Machine Learning, TensorFlow, and Data Analysis.";
  
  } else if (role.includes("cloud")) {
    jobDesc.value = "We are looking for a Cloud Engineer with skills in AWS, Google Cloud, DevOps, and deployment.";
  
  } else {
    jobDesc.value = `We are looking for candidates for the role of ${role}. The candidate should have strong technical skills, problem solving ability, and good communication skills.`;
  }
});