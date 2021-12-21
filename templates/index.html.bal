<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Prevoyance</title>
    <script src="//cdn.bootcss.com/mathjax/2.7.0/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
    <script src="//libs.baidu.com/jquery/1.10.2/jquery.min.js"></script>
    <script>
        $(document).ready(function () {
            $("#parameter-c").hide();
            $("#parameter-d").hide();
        });

        function initParameterInputer(model) {
            if (model === "Model1") {
                if ($("#parameter-c").is(":visible")) {
                    $("#parameter-c").hide();
                }
                if ($("#parameter-d").is(":visible")) {
                    $("#parameter-d").hide();
                }
            } else if (model === "Model2") {
                if ($("#parameter-c").is(":visible")) {
                    $("#parameter-c").hide();
                }
                if ($("#parameter-d").is(":hidden")) {
                    $("#parameter-d").show();
                }
            } else if (model === "Model3") {
                if($("#parameter-c").is(":hidden")){
                    $("#parameter-c").show();
                }
                if ($("#parameter-d").is(":visible")) {
                    $("#parameter-d").hide();
                }
            } else if (model === "Model4") {
                if ($("#parameter-c").is(":hidden")) {
                    $("#parameter-c").show();
                }
                if ($("#parameter-d").is(":hidden")) {
                    $("#parameter-d").show();
                }
            }
        }

        $(document).ready(function () {
            $('input[type=radio][name=model]').change(function () {
                if (this.value === 'Model1') {
                    initParameterInputer('Model1');
                } else if (this.value === 'Model2') {
                    initParameterInputer('Model2');
                } else if (this.value === 'Model3') {
                    initParameterInputer('Model3');
                } else if (this.value === 'Model4') {
                    initParameterInputer('Model4');
                }
            });
        });

    </script>
    <style>
        .designArea {
            border: 2px #f2f2f2 dotted;
            background-color: #f7f7f7;
            width: 85%;
            overflow: auto;
            margin: 0 auto;
        }

        #parameter {
            background-color: #f2f2f2;
            width: 30%;
            border: 2px #f1f1f1 double;
            float: left;
            margin: 1%;
        }

        #plot {
            background-color: #f7f7f7;
            width: 55%;
            float: right;
            margin: 1%;

        }
    </style>

</head>
<body>
<h1>
    Prevoyance
</h1>
<br>
<b>Description:</b> Prevoyance is an application that can compute D-optimal designs for Dose-Response design which can
be
described by a general family of models.
<br>
<b>Models:</b>
<p>$$\text{Model 1:}\quad y = a \exp{(x/b)} \text{ with }a>0$$</p>
<p>$$\text{Model 2:}\quad y = a \exp{(\pm(x/b)^d)} \text{ with }a>0, b>0, d\geq1$$</p>
<p>$$\text{Model 3:}\quad y = a [c - (c -1)\exp{(-x/b)}] \text{ with }a>0, b>0, c>0$$</p>
<p>$$\text{Model 4:}\quad y = a [c - (c -1)\exp{-(x/b)^d}] \text{ with }a>0, b>0, c>0,d\geq1$$</p>
<p>This four models can be used for describing the change in any continuous endpoint as a function of dose.</p>
<p>\(y\) is any continuous endpoint, and \(x\) denotes the dose. </p>
<p>In all models the parameter \(a\) represents the level of the endpoint at dose 0, and \(b\) can be considered as the
    parameter reﬂecting the efﬁcacy of the chemical (or the sensitivity of the subject).</p>
<p>At high doses Models 3 and 4 level off to the value \(ac\), so the parameter \(c\) can be interpreted as the maximum
    relative change.</p>
<p>The parameter \(d\) is constrained to values \(\geq\) 1, to prevent the slope of the function at dose 0 being
    inﬁnite, which seems biologically implausible.</p>
<br>
<div class="designArea">
    <div id="parameter">
        <b>Models:</b>
        <br>
        <form>
            <input type="radio" name="model" value="Model1">Model 1<br>
            <input type="radio" name="model" value="Model2">Model 2<br>
            <input type="radio" name="model" value="Model3">Model 3<br>
            <input type="radio" name="model" value="Model4">Model 4
        </form>

        <form id="parameter-inputer">
            <b>Parameters:</b>
            <br>
            <div id="parameter-a">
                <label for="parameter-a-inputer">a:</label>
                <input type="text" id="parameter-a-inputer" value="1">
                <br>
            </div>
            <div id="parameter-b">
                <label for="parameter-b-inputer">b:</label>
                <input type="text" id="parameter-b-inputer" value="1">
                <br>
            </div>
            <div id="parameter-c">
                <label for="parameter-c-inputer">c:</label>
                <input type="text" id="parameter-c-inputer" value="1">
                <br>
            </div>
            <div id="parameter-d">
                <label for="parameter-d-inputer">d:</label>
                <input type="text" id="parameter-d-inputer" value="1">
                <br>
            </div>
            <input type="button" value="Submit" onclick="submit()">
        </form>
    </div>
    <div id="plot">

    </div>


</div>

</body>
</html>