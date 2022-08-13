function createPost() {
  form = document.getElementById("post");

  headingLabel = document.createElement("label");
  headingLabel.setAttribute("for", "heading");
  msg = document.createTextNode('Heading of the Post:')
  headingLabel.appendChild(msg)

  headingInput = document.createElement("input");
  headingInput.setAttribute("id", "heading");
  headingInput.setAttribute("name", "heading");
  headingInput.setAttribute("placeholder", "Enter the heading of the Post");
  headingInput.setAttribute("class", "form-control w-50");


  postLabel = document.createElement("label");
  postLabel.setAttribute("for", "post");
  msg = document.createTextNode('Post:')
  postLabel.appendChild(msg)

  post = document.createElement('textarea')
  post.setAttribute('id', 'post')
  post.setAttribute('name', 'post')
  post.setAttribute('placeholder', 'Write your Post')
  post.setAttribute('class', 'form-control w-50')
  post.setAttribute("cols", "30");
  post.setAttribute("rows", "15");

  button = document.createElement('button')
  button.setAttribute('class','btn btn-primary')
  msg = document.createTextNode('Create Post')
  button.appendChild(msg)
  
  form.appendChild(headingLabel);
  form.appendChild(headingInput);
  form.appendChild(postLabel);
  form.appendChild(post);
  form.appendChild(button)
}
