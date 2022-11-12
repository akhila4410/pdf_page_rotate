content = """
    <head>
    <style>
    .center {
              text-align: center;
              color: red;
              font-size:50px;
            }
    .center1 {
              text-align: center;
              color: black;
              font-size:30px;
            }
    .button {
              border: none;
              display: flex;
              color: #4CAF50;
              padding: 40px 70px;
              text-align: center;
              text-decoration: none;
              display: inline-block;
              font-size: 35px;
              margin: 4px 2px;
              cursor: pointer;
              border: 2px solid #4CAF50;
              justify-content: center;
            }
    .center2 {
              margin: 0;
              position: absolute;
              top: 50%;
              left: 50%;
              -ms-transform: translate(-50%, -50%);
              transform: translate(-50%, -50%);
            }
    .button1:hover {
                  background-color: #4CAF50;
                  color: white;
                  }
    </style>
    </head>
    <body style="background-color:powderblue;">
    <p class = "center"> PDF_ROTATE-API</p> 
    <p class = "center1"> Rotate the page you like at a specified angle </p>
    <a href = "http://127.0.0.1:8080/docs">
    <div class="center2"><button class = "button button1" > Browse file </button></div>
    </a>
    </body>
    """
