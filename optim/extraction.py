import json
from typing import Optional

from kor import create_extraction_chain
from kor import from_pydantic
from pydantic import BaseModel, Field

from optim.llm_loader import main as llm_loader


# Pydantic data class
class Symptoms1(BaseModel):
    # Symptoms
    itching: Optional[bool] = Field(description="Does the patient have the symptom of itching?")
    skin_rash: Optional[bool] = Field(description="Does the patient have the symptom of skin rash?")
    nodal_skin_eruptions: Optional[bool] = Field(
        description="Does the patient have the symptom of nodal skin eruptions?")
    continuous_sneezing: Optional[bool] = Field(description="Does the patient have the symptom of continuous sneezing?")
    shivering: Optional[bool] = Field(description="Does the patient have the symptom of shivering?")
    chills: Optional[bool] = Field(description="Does the patient have the symptom of chills?")
    joint_pain: Optional[bool] = Field(description="Does the patient have the symptom of joint pain?")
    stomach_pain: Optional[bool] = Field(description="Does the patient have the symptom of stomach pain?")
    acidity: Optional[bool] = Field(description="Does the patient have the symptom of acidity?")
    ulcers_on_tongue: Optional[bool] = Field(description="Does the patient have the symptom of ulcers on tongue?")
    muscle_wasting: Optional[bool] = Field(description="Does the patient have the symptom of muscle wasting?")
    vomiting: Optional[bool] = Field(description="Does the patient have the symptom of vomiting?")
    burning_micturition: Optional[bool] = Field(description="Does the patient have the symptom of burning micturition?")
    spotting_urination: Optional[bool] = Field(description="Does the patient have the symptom of spotting urination?")
    fatigue: Optional[bool] = Field(description="Does the patient have the symptom of fatigue?")
    weight_gain: Optional[bool] = Field(description="Does the patient have the symptom of weight gain?")
    anxiety: Optional[bool] = Field(description="Does the patient have the symptom of anxiety?")
    cold_hands_and_feets: Optional[bool] = Field(
        description="Does the patient have the symptom of cold hands and feet?")
    mood_swings: Optional[bool] = Field(description="Does the patient have the symptom of mood swings?")
    weight_loss: Optional[bool] = Field(description="Does the patient have the symptom of weight loss?")
    restlessness: Optional[bool] = Field(description="Does the patient have the symptom of restlessness?")
    lethargy: Optional[bool] = Field(description="Does the patient have the symptom of lethargy?")
    patches_in_throat: Optional[bool] = Field(description="Does the patient have the symptom of patches in throat?")


class Symptoms2(BaseModel):
    irregular_sugar_level: Optional[bool] = Field(
        description="Does the patient have the symptom of irregular sugar level?")
    cough: Optional[bool] = Field(description="Does the patient have the symptom of cough?")
    high_fever: Optional[bool] = Field(description="Does the patient have the symptom of high fever?")
    sunken_eyes: Optional[bool] = Field(description="Does the patient have the symptom of sunken eyes?")
    breathlessness: Optional[bool] = Field(description="Does the patient have the symptom of breathlessness?")
    sweating: Optional[bool] = Field(description="Does the patient have the symptom of sweating?")
    dehydration: Optional[bool] = Field(description="Does the patient have the symptom of dehydration?")
    indigestion: Optional[bool] = Field(description="Does the patient have the symptom of indigestion?")
    headache: Optional[bool] = Field(description="Does the patient have the symptom of headache?")
    yellowish_skin: Optional[bool] = Field(description="Does the patient have the symptom of yellowish skin?")
    dark_urine: Optional[bool] = Field(description="Does the patient have the symptom of dark urine?")
    nausea: Optional[bool] = Field(description="Does the patient have the symptom of nausea?")
    loss_of_appetite: Optional[bool] = Field(description="Does the patient have the symptom of loss of appetite?")
    pain_behind_the_eyes: Optional[bool] = Field(
        description="Does the patient have the symptom of pain behind the eyes?")
    back_pain: Optional[bool] = Field(description="Does the patient have the symptom of back pain?")
    constipation: Optional[bool] = Field(description="Does the patient have the symptom of constipation?")
    abdominal_pain: Optional[bool] = Field(description="Does the patient have the symptom of abdominal pain?")
    diarrhoea: Optional[bool] = Field(description="Does the patient have the symptom of diarrhoea?")
    mild_fever: Optional[bool] = Field(description="Does the patient have the symptom of mild fever?")
    yellow_urine: Optional[bool] = Field(description="Does the patient have the symptom of yellow urine?")
    yellowing_of_eyes: Optional[bool] = Field(description="Does the patient have the symptom of yellowing of eyes?")
    acute_liver_failure: Optional[bool] = Field(description="Does the patient have the symptom of acute liver failure?")
    fluid_overload: Optional[bool] = Field(description="Does the patient have the symptom of fluid overload?")
    swelling_of_stomach: Optional[bool] = Field(description="Does the patient have the symptom of swelling of stomach?")
    swelled_lymph_nodes: Optional[bool] = Field(description="Does the patient have the symptom of swelled lymph nodes?")
    malaise: Optional[bool] = Field(description="Does the patient have the symptom of malaise?")
    blurred_and_distorted_vision: Optional[bool] = Field(
        description="Does the patient have the symptom of blurred and distorted vision?")
    phlegm: Optional[bool] = Field(description="Does the patient have the symptom of phlegm?")
    throat_irritation: Optional[bool] = Field(description="Does the patient have the symptom of throat irritation?")
    redness_of_eyes: Optional[bool] = Field(description="Does the patient have the symptom of redness of eyes?")
    sinus_pressure: Optional[bool] = Field(description="Does the patient have the symptom of sinus pressure?")
    runny_nose: Optional[bool] = Field(description="Does the patient have the symptom of runny nose?")
    congestion: Optional[bool] = Field(description="Does the patient have the symptom of congestion?")
    chest_pain: Optional[bool] = Field(description="Does the patient have the symptom of chest pain?")
    weakness_in_limbs: Optional[bool] = Field(description="Does the patient have the symptom of weakness in limbs?")
    fast_heart_rate: Optional[bool] = Field(description="Does the patient have the symptom of fast heart rate?")


class Symptoms3(BaseModel):
    pain_during_bowel_movements: Optional[bool] = Field(
        description="Does the patient have the symptom of pain during bowel movements?")
    pain_in_anal_region: Optional[bool] = Field(description="Does the patient have the")
    bloody_stool: Optional[bool] = Field(description="Does the patient have the symptom of bloody stool?")
    irritation_in_anus: Optional[bool] = Field(description="Does the patient have the symptom of irritation in anus?")
    neck_pain: Optional[bool] = Field(description="Does the patient have the symptom of neck pain?")
    dizziness: Optional[bool] = Field(description="Does the patient have the symptom of dizziness?")
    cramps: Optional[bool] = Field(description="Does the patient have the symptom of cramps?")
    bruising: Optional[bool] = Field(description="Does the patient have the symptom of bruising?")
    obesity: Optional[bool] = Field(description="Does the patient have the symptom of obesity?")
    swollen_legs: Optional[bool] = Field(description="Does the patient have the symptom of swollen legs?")
    swollen_blood_vessels: Optional[bool] = Field(
        description="Does the patient have the symptom of swollen blood vessels?")
    puffy_face_and_eyes: Optional[bool] = Field(description="Does the patient have the symptom of puffy face and eyes?")
    enlarged_thyroid: Optional[bool] = Field(description="Does the patient have the symptom of enlarged thyroid?")
    brittle_nails: Optional[bool] = Field(description="Does the patient have the symptom of brittle nails?")
    swollen_extremeties: Optional[bool] = Field(description="Does the patient have the symptom of swollen extremeties?")
    excessive_hunger: Optional[bool] = Field(description="Does the patient have the symptom of excessive hunger?")
    extra_marital_contacts: Optional[bool] = Field(
        description="Does the patient have the symptom of extra marital contacts?")
    drying_and_tingling_lips: Optional[bool] = Field(
        description="Does the patient have the symptom of drying and tingling lips?")
    slurred_speech: Optional[bool] = Field(description="Does the patient have the symptom of slurred speech?")
    knee_pain: Optional[bool] = Field(description="Does the patient have the symptom of knee pain?")
    hip_joint_pain: Optional[bool] = Field(description="Does the patient have the symptom of hip joint pain?")
    muscle_weakness: Optional[bool] = Field(description="Does the patient have the symptom of muscle weakness?")
    stiff_neck: Optional[bool] = Field(description="Does the patient have the symptom of stiff neck?")
    swelling_joints: Optional[bool] = Field(description="Does the patient have the symptom of swelling joints?")
    movement_stiffness: Optional[bool] = Field(description="Does the patient have the symptom of movement stiffness?")
    spinning_movements: Optional[bool] = Field(description="Does the patient have the symptom of spinning movements?")
    loss_of_balance: Optional[bool] = Field(description="Does the patient have the symptom of loss of balance?")
    unsteadiness: Optional[bool] = Field(description="Does the patient have the symptom of unsteadiness?")
    weakness_of_one_body_side: Optional[bool] = Field(
        description="Does the patient have the symptom of weakness of one body side?")
    loss_of_smell: Optional[bool] = Field(description="Does the patient have the symptom of loss of smell?")
    bladder_discomfort: Optional[bool] = Field(description="Does the patient have the symptom of bladder discomfort?")
    foul_smell_ofurine: Optional[bool] = Field(description="Does the patient have the symptom of foul smell of urine?")
    continuous_feel_of_urine: Optional[bool] = Field(
        description="Does the patient have the symptom of continuous feel of urine?")
    passage_of_gases: Optional[bool] = Field(description="Does the patient have the symptom of passage of gases?")
    internal_itching: Optional[bool] = Field(description="Does the patient have the symptom of internal itching?")
    toxic_look_typhos: Optional[bool] = Field(description="Does the patient have the symptom of toxic look typhos?")
    depression: Optional[bool] = Field(description="Does the patient have the symptom of depression?")
    irritability: Optional[bool] = Field(description="Does the patient have the symptom of irritability?")
    muscle_pain: Optional[bool] = Field(description="Does the patient have the symptom of muscle pain?")
    altered_sensorium: Optional[bool] = Field(description="Does the patient have the symptom of altered sensorium?")
    red_spots_over_body: Optional[bool] = Field(description="Does the patient have the symptom of red spots over body?")
    belly_pain: Optional[bool] = Field(description="Does the patient have the symptom of belly pain?")
    abnormal_menbooluation: Optional[bool] = Field(
        description="Does the patient have the symptom of abnormal menbooluation?")
    dischromic_patches: Optional[bool] = Field(description="Does the patient have the symptom of dischromic patches?")
    watering_from_eyes: Optional[bool] = Field(description="Does the patient have the symptom of watering from eyes?")
    increased_appetite: Optional[bool] = Field(description="Does the patient have the symptom of increased appetite?")
    polyuria: Optional[bool] = Field(description="Does the patient have the symptom of polyuria?")
    family_history: Optional[bool] = Field(description="Does the patient have the symptom of family history?")
    mucoid_sputum: Optional[bool] = Field(description="Does the patient have the symptom of mucoid sputum?")
    rusty_sputum: Optional[bool] = Field(description="Does the patient have the symptom of rusty sputum?")
    lack_of_concentration: Optional[bool] = Field(
        description="Does the patient have the symptom of lack of concentration?")
    visual_disturbances: Optional[bool] = Field(description="Does the patient have the symptom of visual disturbances?")
    receiving_blood_transfusion: Optional[bool] = Field(
        description="Does the patient have the symptom of receiving blood transfusion?")


class Symptoms4(BaseModel):
    coma: Optional[bool] = Field(description="Does the patient have the symptom of coma?")
    stomach_bleeding: Optional[bool] = Field(description="Does the patient have the symptom of stomach bleeding?")
    distention_of_abdomen: Optional[bool] = Field(
        description="Does the patient have the symptom of distention of abdomen?")
    history_of_alcohol_consumption: Optional[bool] = Field(
        description="Does the patient have the symptom of history of alcohol consumption?")
    receiving_unsterile_injections: Optional[bool] = Field(
        description="Does the patient have the symptom of receiving unsterile injections?")
    blood_in_sputum: Optional[bool] = Field(description="Does the patient have the symptom of blood in sputum?")
    prominent_veins_on_calf: Optional[bool] = Field(
        description="Does the patient have the symptom of prominent veins on calf?")
    palpitations: Optional[bool] = Field(description="Does the patient have the symptom of palpitations?")
    painful_walking: Optional[bool] = Field(description="Does the patient have the symptom of painful walking?")
    pus_filled_pimples: Optional[bool] = Field(description="Does the patient have the symptom of pus filled pimples?")
    blackheads: Optional[bool] = Field(description="Does the patient have the symptom of blackheads?")
    scurring: Optional[bool] = Field(description="Does the patient have the symptom of scurring?")
    red_sore_around_nose: Optional[bool] = Field(
        description="Does the patient have the symptom of red sore around nose?")
    skin_peeling: Optional[bool] = Field(description="Does the patient have the symptom of skin peeling?")
    silver_like_dusting: Optional[bool] = Field(description="Does the patient have the symptom of silver like dusting?")
    small_dents_in_nails: Optional[bool] = Field(
        description="Does the patient have the symptom of small dents in nails?")
    inflammatory_nails: Optional[bool] = Field(description="Does the patient have the symptom of inflammatory nails?")
    blister: Optional[bool] = Field(description="Does the patient have the symptom of blister?")
    yellow_crust_ooze: Optional[bool] = Field(description="Does the patient have the symptom of yellow crust ooze?")
    prognosis: Optional[bool] = Field(description="Does the patient have the symptom of prognosis?")


# open the template file
with open("Data/extraction_prompt.txt", "r") as f:
    QUERY = f.read()


def main(conversation: str):
    llm = llm_loader()
    symptoms_extraction = {}
    # iterate on Symptoms classes
    for symptoms in [(Symptoms1, "symptoms1"), (Symptoms2, "symptoms2"), (Symptoms3, "symptoms3"),
                     (Symptoms4, "symptoms4")]:
        schema, validator = from_pydantic(symptoms[0])
        # Extraction
        chain = create_extraction_chain(
            llm, schema, encoder_or_encoder_class="json", validator=validator
        )
        query = f"""Please extract the patient's different syntone from this conversation.\n\n Please confirm the 
        presence of these symptoms with a Boolean (True or False).\n\n Do NOT include any additional information. The 
        output MUST follow the above scheme. Do NOT add any additional columns that are not included in the scheme.\n\n
         {conversation}"""
        extraction = chain.run(query)["raw"]
        extraction = json.loads(extraction)
        print(type(extraction))
        symptoms_extraction.update(extraction)
        return symptoms_extraction
