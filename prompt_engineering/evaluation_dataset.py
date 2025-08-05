"""Dataset de evaluación para testing de prompts en fintech."""

EVALUATION_DATASET = [
  {
    "question": "¿Dónde puedo ver los límites de mi tarjeta de débito?",
    "ideal_answer": "¡Hola! Gracias por tu consulta. Podés ver y ajustar los límites diarios de tu tarjeta de débito desde nuestra app, en la sección 'Límites'. Allí vas a encontrar opciones para modificar montos tanto de compras como de extracciones, de forma temporal o permanente. Si necesitás ayuda con el proceso, estamos para acompañarte.",
    "category": "tarjeta_debito"
  },
  {
    "question": "¿Qué hago si se me olvidó el PIN de mi tarjeta de débito?",
    "ideal_answer": "¡Hola! No te preocupes, podés restablecer tu PIN directamente desde nuestra app. Ingresá a 'Tarjetas', seleccioná tu tarjeta de débito y elegí la opción para cambiar el PIN. El proceso es rápido y seguro. Si necesitás una guía paso a paso, escribinos por el chat y te ayudamos.",
    "category": "tarjeta_debito"
  },
  {
    "question": "¿Puedo usar la tarjeta de débito en el exterior?",
    "ideal_answer": "¡Hola! Sí, podés usar tu tarjeta de débito en el exterior tanto para compras en comercios como para extracciones en cajeros. El límite diario para retiros es de USD 500 y se aplica una comisión de USD 2,5 por transacción. Te recomendamos avisarnos desde la app antes de viajar para evitar bloqueos preventivos por seguridad.",
    "category": "tarjeta_debito"
  },
  {
    "question": "¿La tarjeta de débito tiene algún costo mensual?",
    "ideal_answer": "¡Hola! No, nuestra tarjeta de débito no tiene costo mensual de mantenimiento. Solo se aplican tarifas puntuales, como la reposición por pérdida o robo, y las extracciones en cajeros del exterior. Si tenés dudas sobre algún cargo en particular, escribinos por el chat y lo revisamos juntos.",
    "category": "tarjeta_debito"
  },
  {
    "question": "¿Qué beneficios tiene la tarjeta de débito?",
    "ideal_answer": "¡Hola! Nuestra tarjeta de débito ofrece beneficios como 1 % de cashback en supermercados y participación en sorteos mensuales si tus compras superan los $50.000 ARS. También accedés a promociones temporales en delivery, transporte y plataformas de streaming. Todo sin costo de mantenimiento.",
    "category": "tarjeta_debito"
  },
  {
    "question": "¿Cuáles son los pasos para pedir una tarjeta de crédito?",
    "ideal_answer": "¡Hola! Gracias por tu interés. Para solicitar la tarjeta de crédito, ingresá a nuestra app y completá la solicitud con tus datos e ingresos. Evaluamos tu perfil crediticio y en menos de 24 h te damos una respuesta. Si es aprobada, la tarjeta digital se habilita al instante y la física llega en 5 a 7 días hábiles.",
    "category": "tarjeta_credito"
  },
  {
    "question": "¿Qué pasa si pago mi tarjeta de crédito antes del vencimiento?",
    "ideal_answer": "¡Hola! Si realizás el pago antes del vencimiento, vas a reducir los intereses generados y liberar parte del límite disponible para nuevas compras. Es una buena práctica financiera y podés hacerlo en cualquier momento desde la app.",
    "category": "tarjeta_credito"
  },
  {
    "question": "¿Qué días cierra y vence mi tarjeta de crédito?",
    "ideal_answer": "¡Hola! La fecha de cierre de tu tarjeta de crédito es el día 20 de cada mes, y el vencimiento es el día 10 del mes siguiente. Esto te da hasta 50 días para pagar tus consumos sin interés, dependiendo de cuándo los realices. Podés consultar tu resumen en la app cuando lo necesites.",
    "category": "tarjeta_credito"
  },
  {
    "question": "¿Qué hago si detecto un consumo no reconocido en mi tarjeta de crédito?",
    "ideal_answer": "¡Hola! Si ves un consumo que no reconocés, te sugerimos bloquear la tarjeta desde la app por precaución. Luego, ingresá a 'Ayuda' → 'Desconozco un cargo' para iniciar el reclamo. Nuestro equipo lo investigará y te acompañará en todo el proceso.",
    "category": "tarjeta_credito"
  },
  {
    "question": "¿Cómo se calculan los puntos del programa de recompensas?",
    "ideal_answer": "¡Hola! Cada vez que hacés una compra con tu tarjeta de crédito, sumás 1 punto por cada $200 ARS. Además, los viernes obtenés 2 % de cashback en restaurantes. Los puntos tienen una vigencia de 24 meses y podés canjearlos desde la app por productos, viajes o servicios.",
    "category": "tarjeta_credito"
  },
  {
    "question": "¿Qué puedo hacer desde la app con mi tarjeta de crédito?",
    "ideal_answer": "¡Hola! Desde nuestra app podés ver tus consumos en tiempo real, pagar el resumen, cambiar el PIN, congelar o reactivar la tarjeta, descargar comprobantes y acceder a tus recompensas. Todo de forma simple y segura.",
    "category": "tarjeta_credito"
  },
  {
    "question": "¿Puedo pedir un préstamo desde la app?",
    "ideal_answer": "¡Hola! Sí, podés pedir un préstamo 100 % online. Solo tenés que simular el monto y plazo desde la app, subir tu DNI y recibo de sueldo, y en menos de 2 horas te damos una respuesta. Si es aprobado, el dinero se acredita en tu cuenta en una hora.",
    "category": "prestamo"
  },
  {
    "question": "¿Cuáles son los tipos de préstamo disponibles?",
    "ideal_answer": "¡Hola! Tenemos dos opciones: préstamos a plazo fijo, con cuotas fijas entre 6 y 48 meses; y préstamos flexibles, que te permiten adelantar pagos o cancelar sin penalidades. Ambos están diseñados para adaptarse a tu perfil y necesidades.",
    "category": "prestamo"
  },
  {
    "question": "¿Cómo se pagan las cuotas del préstamo?",
    "ideal_answer": "¡Hola! Las cuotas se debitan automáticamente de tu cuenta el día 5 de cada mes. Si preferís, también podés adelantar pagos desde la app para ahorrar intereses. Siempre te avisamos con anticipación para que estés preparado.",
    "category": "prestamo"
  },
  {
    "question": "¿Qué pasa si no tengo saldo el día del débito del préstamo?",
    "ideal_answer": "¡Hola! Si no hay saldo disponible el día 5, reintentamos el débito 48 horas después. Si el pago sigue pendiente, se aplica un interés por mora del 2 % mensual. Te enviaremos recordatorios para ayudarte a mantenerte al día.",
    "category": "prestamo"
  },
  {
    "question": "¿Puedo cancelar anticipadamente mi préstamo?",
    "ideal_answer": "¡Hola! Sí, podés cancelar tu préstamo anticipadamente sin penalidad. Desde la app podés consultar el monto actualizado y pagar por transferencia. Esto te permite ahorrar intereses y organizar mejor tus finanzas.",
    "category": "prestamo"
  },
  {
    "question": "¿El préstamo incluye seguro de vida?",
    "ideal_answer": "¡Hola! Sí, todos nuestros préstamos incluyen un seguro de vida que cubre el saldo pendiente en caso de fallecimiento. El costo ya está incorporado en cada cuota, por lo que no hay cargos extra.",
    "category": "prestamo"
  },
  {
    "question": "¿Cuál es el CFT del préstamo?",
    "ideal_answer": "¡Hola! El Costo Financiero Total (CFT) incluye la tasa de interés, el seguro de vida y todos los cargos asociados. Te mostramos el monto total a devolver antes de aceptar el préstamo, para que tomes una decisión informada.",
    "category": "prestamo"
  },
  {
    "question": "¿Qué pasa si quiero pedir otro préstamo y ya tengo uno vigente?",
    "ideal_answer": "¡Hola! Podés solicitar un segundo préstamo si tu ratio de endeudamiento es menor al 40 % y llevás al menos 6 cuotas pagas al día. Desde la app evaluamos tu perfil y te informamos si calificás.",
    "category": "prestamo"
  },
  {
    "question": "¿Qué consejos dan antes de pedir un préstamo?",
    "ideal_answer": "¡Hola! Antes de pedir un préstamo, te recomendamos que la cuota no supere el 30 % de tus ingresos mensuales y que mantengas un fondo de emergencia. Es importante usar el préstamo para objetivos claros y evitar sobreendeudarte.",
    "category": "prestamo"
  }
]


def get_dataset():
    return EVALUATION_DATASET

def get_questions_by_category(category):
    return [item for item in EVALUATION_DATASET if item["category"] == category]

def get_all_questions():
    return [item["question"] for item in EVALUATION_DATASET]

def get_all_ideal_answers():
    return [item["ideal_answer"] for item in EVALUATION_DATASET]