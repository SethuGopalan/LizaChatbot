from chatterbot import ChatBot
import chatterbot
import dash
from dash import dcc, html, callback, Input, Output,State
import dash_bootstrap_components as dbc
import requests

from chatterbot.logic import LogicAdapter


from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer

# chatbot=ChatBot("My Liza")

chatbot = ChatBot(
    'Liza',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)
chatbot.storage.drop()

logic_adapters=[



        {
    
            "import_path": "chatterbot.logic.BestMatch",
            # "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance,
            # "response_selection_method": chatterbot.response_selection.get_first_response
            'default_response': 'I am sorry, but I do not understand.',
          
            'maximum_similarity_threshold': 0.90

        }


    ]


conversations={

    "hello",
    "Hi There",
    "How are you doing",
    "I am doing great",
    "That is good to hear",
    "Thank you",
    "you are welcome"
}
# trainer =ListTrainer(chatbot)
# trainer.train(conversations)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    'chatterbot_corpus\data\english'
) 

# resp=input()

# resporesponse(resp)

# print(response)



app=dash.Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ])

app.layout=dbc.Container([

   dbc.Row([

    dbc.Col([
    
    html.Div([
     html.Br(),
     html.Br(),
     html.Br(),
    
     html.H5(" Hey I am Liza "),
     dcc.Input(id="input_Id",type="text",placeholder="text",value=""),
     

     html.Button(id='submit-button', type='submit', children='Submit'),
     html.Br(),
     html.Br(),
     html.Div(id="outpit_id",style={
                     'font-family': 'Sans-serif', 'color': 'white', 'fontSize': 14}),
     
        
    ]),

    
     
    ])

   ])
])

@app.callback(Output("outpit_id",'children'),
            #   Output("input_Id","children"),
                  Input('submit-button', 'n_clicks'),
                  State("input_Id","value"),
                  
                  )
            


def responce_update(clicks,resp):

        
    
    if clicks is not None:

        
        # input=clear                          
        response=chatbot.get_response(resp)
             
        return html.Div([html.P("Me : {}".format(resp))],style={
                      'color': 'yellow'}),html.Div([html.P("Liza : {}".format(response))],style={
                      'color': 'whitle'})
    # else:
    #     clear=""
            


if __name__ == "__main__":
    app.run_server(debug=True, port=8051)     