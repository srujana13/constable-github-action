
let timer = null;

const repoInputElement = document.getElementById("repo");
const submitBtnElement = document.getElementById("submitBtn");

repoInputElement.addEventListener("keydown", () => {
  clearTimeout(timer); 
  timer = setTimeout(checkValidRepo, 1000);
});

const checkValidRepo = () => {
    isValidRepo = false;
    submitBtnElement.setAttribute("disabled", true);
    const repo_name = repoInputElement.value;

    const setRepoClass = async (repo_name) => {
        repoInputElement.classList.add("loading");
        repoInputElement.classList.remove("valid");
        repoInputElement.classList.remove("invalid");
        const response = await fetch(`/check_repo?repo=${repo_name}`);
        const myJson = await response.json();
        if (myJson['valid']) {
            repoInputElement.classList.remove("loading");
            repoInputElement.classList.add("valid");
            
    submitBtnElement.removeAttribute("disabled");
        }
        else {
            repoInputElement.classList.remove("loading");
            repoInputElement.classList.add("invalid");
            isValidRepo = false;

    submitBtnElement.setAttribute("disabled", true);
        }
    };
    setRepoClass(repo_name);

}

const getScore = () => {
    document.getElementById("results").classList.add("hidden");
    document.getElementById("spinner").classList.remove("hidden");
    const repo_name = repoInputElement.value;
    const setScoreValue = async (repo_name) => {
    const response = await fetch(`/get_score?repo=${repo_name}`);
    const scoreJson = await response.json();
    document.getElementById("score_json").innerHTML = JSON.stringify(scoreJson);
    document.getElementById("markdown").innerHTML = `![Constable](${scoreJson['badge']})`;
    document.getElementById("spinner").classList.add("hidden");
    document.getElementById("results").classList.remove("hidden");
    };
    setScoreValue(repo_name);
}