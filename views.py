from flask import Blueprint, render_template, redirect

views=Blueprint(__name__,"views")



@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/projects")
def projects():
    return render_template("projectsnav.html")

@views.route("/hestoncall")
def heston():
    return redirect("https://github.com/diracdyson/HESTON/blob/main/fromscratchHESTON.ipynb",code=302)

@views.route("/garch")
def garch():
    return redirect("https://github.com/diracdyson/VaRGARCH/blob/main/fromscratchGARCH.ipynb",code=302)

@views.route("/ppomario")
def ppomario():
    return redirect("https://github.com/diracdyson/policygrad/blob/main/numpyjawncartpole.ipynb",code=302)

@views.route("/pairs")
def pairs():
    return redirect("https://github.com/diracdyson/pairsCIR/blob/main/pairs_trading.ipynb",code=302)

@views.route("/lstmq")
def lstmq():
    return redirect("https://github.com/diracdyson/LSTM-Q/blob/main/Keras(LSTM-Q).ipynb",code=302)
@views.route("/lstm")
def lstm():
    return redirect("https://github.com/diracdyson/LSTM-pytorch/blob/main/LSTMPYTORCH.ipynb",code=302)
@views.route("/supportvec")
def supportvec():
    return redirect("https://github.com/diracdyson/SUpportvectorregressor/blob/main/svr.ipynb",code=302)
@views.route("/kmeans")
def kmeans():
    return redirect("https://github.com/diracdyson/roughkmeans/blob/main/kmeansandclassifying.ipynb",code=302)
@views.route("/vqe")
def vqe():
    return redirect("https://docs.google.com/presentation/d/1V0yeUz6cT_NMeg_hF4QU5NyeWVhz496b/edit?usp=sharing&ouid=104133140955889917444&rtpof=true&sd=true",code=302)

@views.route("/vqeforH")
def vqeforH():
    return redirect("https://github.com/diracdyson/vqeh2neutralspsa",code=302)

@views.route("/blogs")
def blogs():
    return render_template("blogsnav.html")

@views.route("/youtube")
def youtube():
    return redirect("https://www.youtube.com/channel/UCOlwc2lxpPlNatIC9ystC0A/featured", code=302)

@views.route("/github")
def github():
    return redirect("https://github.com/diracdyson", code=302)


